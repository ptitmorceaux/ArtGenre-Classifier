import pytest
from engine.interop.array import ArrayFloat32Ptr


class TestArrayCreation:
    """Tests de création de tableaux"""
    
    def test_init_with_list(self):
        data = [1.5, 2.5, 3.5]
        arr = ArrayFloat32Ptr(data)
        assert arr.array == data
    
    def test_init_from_incrementing_numbers(self):
        expected = [0.0, 1.0, 2.0, 3.0, 4.0]
        arr = ArrayFloat32Ptr.init_from_incrementing_numbers(5)
        assert arr.array == expected
    
    def test_init_with_integers(self):
        """Les entiers doivent être acceptés et convertis en float"""
        data = [1, 2, 3]
        arr = ArrayFloat32Ptr(data)
        assert arr.array == [1, 2, 3]
    
    def test_init_empty_list_raises_error(self):
        """Une liste vide doit lever une TypeError"""
        with pytest.raises(TypeError, match="non-empty list"):
            ArrayFloat32Ptr([])
    
    def test_init_invalid_types_raises_error(self):
        """Une liste avec des types invalides doit lever une TypeError"""
        with pytest.raises(TypeError, match="must be floats"):
            ArrayFloat32Ptr([1.0, "test", 3.0])
    
    def test_init_large_array(self):
        """Test avec un gros tableau"""
        arr = ArrayFloat32Ptr.init_from_incrementing_numbers(1000)
        assert len(arr.array) == 1000
        assert arr.array[0] == 0.0
        assert arr.array[999] == 999.0


class TestArrayOperations:
    """Tests des opérations sur les tableaux"""
    
    def test_sum_simple(self):
        arr = ArrayFloat32Ptr([1.0, 2.0, 3.0, 4.0])
        assert arr.sum() == 10.0
    
    def test_sum_negative_numbers(self):
        arr = ArrayFloat32Ptr([-1.0, -2.0, -3.0])
        assert arr.sum() == -6.0
    
    def test_sum_mixed_numbers(self):
        arr = ArrayFloat32Ptr([10.0, -5.0, 3.0])
        assert arr.sum() == 8.0
    
    def test_sum_large_array(self):
        arr = ArrayFloat32Ptr.init_from_incrementing_numbers(1000)
        expected = sum(range(1000))  # 0+1+2+...+999 = 499500
        assert arr.sum() == expected


class TestArrayAccess:
    """Tests d'accès aux éléments"""
    
    def test_array_property_get(self):
        arr = ArrayFloat32Ptr([1.0, 2.0, 3.0])
        assert arr.array[0] == 1.0
        assert arr.array[1] == 2.0
        assert arr.array[2] == 3.0
    
    def test_array_property_set(self):
        arr = ArrayFloat32Ptr([1.0, 2.0, 3.0])
        arr.array = [10.0, 20.0, 30.0]
        assert arr.array == [10.0, 20.0, 30.0]
        assert arr.sum() == 60.0
    
    def test_array_index_out_of_bounds(self):
        arr = ArrayFloat32Ptr([1.0, 2.0])
        with pytest.raises(IndexError):
            _ = arr.array[10]
    
    def test_array_modification_affects_sum(self):
        """Vérifier que modifier array met à jour le tableau C"""
        arr = ArrayFloat32Ptr([1.0, 2.0, 3.0])
        assert arr.sum() == 6.0
        
        arr.array = [10.0, 20.0]
        assert arr.sum() == 30.0


class TestArrayValidation:
    """Tests de validation des entrées"""
    
    def test_invalid_length_type(self):
        """init_from_incrementing_numbers doit valider le type de length"""
        with pytest.raises(TypeError):
            ArrayFloat32Ptr.init_from_incrementing_numbers("not a number")
    
    def test_length_too_large(self):
        """Une length > uint32_max doit lever une ValueError"""
        with pytest.raises(ValueError, match="out of bounds"):
            ArrayFloat32Ptr.init_from_incrementing_numbers(5_000_000_000)
    
    def test_set_array_with_invalid_type(self):
        """Setter de array doit valider le type"""
        arr = ArrayFloat32Ptr([1.0, 2.0])
        with pytest.raises(TypeError):
            arr.array = "not a list"
    
    def test_set_array_with_invalid_elements(self):
        """Setter de array doit valider les éléments"""
        arr = ArrayFloat32Ptr([1.0, 2.0])
        with pytest.raises(TypeError):
            arr.array = [1.0, None, 3.0]


class TestArrayMemoryManagement:
    """Tests de gestion mémoire (pas de leaks)"""
    
    def test_multiple_allocations(self):
        """Créer et détruire plusieurs tableaux ne doit pas causer de leak"""
        for _ in range(100):
            arr = ArrayFloat32Ptr.init_from_incrementing_numbers(100)
            _ = arr.sum()
    
    def test_reassignment(self):
        """Réassigner array plusieurs fois ne doit pas causer de leak"""
        arr = ArrayFloat32Ptr([1.0, 2.0])
        for i in range(100):
            arr.array = [float(i), float(i+1), float(i+2)]
