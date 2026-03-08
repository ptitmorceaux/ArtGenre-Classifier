import pytest
import engine.interop.random as Random


class TestRandomOperations:
    """Tests pour les opérations de génération de nombres aléatoires"""
    
    def test_random_float32_basic(self):
        """Test génération basique entre 0 et 1"""
        result = Random.random_float32(0.0, 1.0)
        assert 0.0 <= result <= 1.0
    
    def test_random_float32_range(self):
        """Test génération dans différents intervalles"""
        result = Random.random_float32(10.0, 20.0)
        assert 10.0 <= result <= 20.0
        
        result = Random.random_float32(-10.0, 10.0)
        assert -10.0 <= result <= 10.0
    
    def test_random_float32_inverted_range(self):
        """Test avec min > max (devrait inverser automatiquement)"""
        result = Random.random_float32(20.0, 10.0)
        assert 10.0 <= result <= 20.0
    
    def test_random_float32_equal_bounds(self):
        """Test quand min == max (devrait retourner cette valeur)"""
        result = Random.random_float32(5.0, 5.0)
        assert result == 5.0
        
        result = Random.random_float32(0.0, 0.0)
        assert result == 0.0
    
    def test_random_float32_negative_range(self):
        """Test avec des nombres négatifs"""
        result = Random.random_float32(-50.0, -10.0)
        assert -50.0 <= result <= -10.0
        
        result = Random.random_float32(-100.0, -100.0)
        assert result == -100.0
    
    def test_random_float32_large_range(self):
        """Test avec un grand intervalle"""
        result = Random.random_float32(0.0, 1000.0)
        assert 0.0 <= result <= 1000.0


class TestRandomInvalidInputs:
    """Tests pour les entrées invalides"""
    
    def test_random_float32_with_string(self):
        """Vérifie que passer une string lève une TypeError"""
        with pytest.raises(TypeError, match="must be of type float"):
            Random.random_float32("10", 20.0)
        
        with pytest.raises(TypeError, match="must be of type float"):
            Random.random_float32(10.0, "20")
    
    def test_random_float32_with_none(self):
        """Vérifie que passer None lève une TypeError"""
        with pytest.raises(TypeError, match="must be of type float"):
            Random.random_float32(None, 20.0)
        
        with pytest.raises(TypeError, match="must be of type float"):
            Random.random_float32(10.0, None)
    
    def test_random_float32_with_bool(self):
        """Vérifie que passer un booléen lève une TypeError"""
        with pytest.raises(TypeError, match="must be of type float"):
            Random.random_float32(True, 20.0)
        
        with pytest.raises(TypeError, match="must be of type float"):
            Random.random_float32(10.0, False)
    
    def test_random_float32_with_list(self):
        """Vérifie que passer une liste lève une TypeError"""
        with pytest.raises(TypeError, match="must be of type float"):
            Random.random_float32([10.0], 20.0)
        
        with pytest.raises(TypeError, match="must be of type float"):
            Random.random_float32(10.0, [20.0])
    
    def test_random_float32_with_dict(self):
        """Vérifie que passer un dictionnaire lève une TypeError"""
        with pytest.raises(TypeError, match="must be of type float"):
            Random.random_float32({"value": 10.0}, 20.0)
        
        with pytest.raises(TypeError, match="must be of type float"):
            Random.random_float32(10.0, {"value": 20.0})


class TestRandomEdgeCases:
    """Tests des cas limites"""
    
    def test_random_float32_small_range(self):
        """Test avec un très petit intervalle"""
        result = Random.random_float32(1.0, 1.001)
        assert 1.0 <= result <= 1.001
    
    def test_random_float32_zero_bounds(self):
        """Test avec zéro comme borne"""
        result = Random.random_float32(0.0, 10.0)
        assert 0.0 <= result <= 10.0
        
        result = Random.random_float32(-10.0, 0.0)
        assert -10.0 <= result <= 0.0
    
    def test_random_float32_multiple_calls(self):
        """Test que plusieurs appels génèrent des valeurs dans l'intervalle"""
        results = [Random.random_float32(0.0, 100.0) for _ in range(10)]
        for result in results:
            assert 0.0 <= result <= 100.0
    
    def test_random_float32_distribution(self):
        """Test basique de distribution (tous les résultats ne devraient pas être identiques)"""
        results = [Random.random_float32(0.0, 100.0) for _ in range(20)]
        # Au moins 2 valeurs différentes sur 20 essais (proba tres élevée)
        assert len(set(results)) > 1


