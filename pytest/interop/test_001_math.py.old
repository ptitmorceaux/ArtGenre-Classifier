import pytest
import engine.interop.math as Math


class TestMathOperations:
    """Tests pour les opérations mathématiques de base"""
    
    def test_addition(self):
        assert Math.addition(10, 5) == 15.0
        assert Math.addition(-5, 3) == -2.0
        assert Math.addition(0, 0) == 0.0
    
    def test_subtraction(self):
        assert Math.subtraction(10, 5) == 5.0
        assert Math.subtraction(5, 10) == -5.0
        assert Math.subtraction(0, 0) == 0.0
    
    def test_multiplication(self):
        assert Math.multiplication(10, 5) == 50.0
        assert Math.multiplication(-5, 3) == -15.0
        assert Math.multiplication(0, 10) == 0.0
    
    def test_division(self):
        assert Math.division(10, 2) == 5.0
        assert Math.division(9, 3) == 3.0
        assert Math.division(-10, 2) == -5.0
    
    def test_division_by_zero(self):
        """Vérifie que la division par zéro lève une RuntimeError"""
        with pytest.raises(RuntimeError, match="Division by Zero"):
            Math.division(10, 0)
    
    def test_power(self):
        assert Math.power(2, 3) == 8.0
        assert Math.power(5, 2) == 25.0
        assert Math.power(10, 0) == 1.0
        # Note: Les exposants négatifs ne sont pas supportés par l'implémentation C basique


class TestMathEdgeCases:
    """Tests des cas limites"""
    
    def test_large_numbers(self):
        result = Math.addition(1e6, 1e6)
        assert result == 2e6
    
    def test_small_numbers(self):
        result = Math.addition(0.001, 0.002)
        assert abs(result - 0.003) < 1e-6
    
    def test_power_with_base_zero(self):
        result = Math.power(0, 5)
        assert result == 0.0
    
    def test_power_with_base_one(self):
        result = Math.power(1, 100)
        assert result == 1.0
