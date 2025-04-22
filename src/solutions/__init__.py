from .dyscalculia import provide_dyscalculia_solution
# Commentez temporairement cette ligne
# from .enhanced_dyscalculia import provide_enhanced_dyscalculia_solution
from .improved_dyscalculia import provide_improved_dyscalculia_solution
from .tdah import provide_tdah_solution

__all__ = [
    'provide_dyscalculia_solution', 
    # 'provide_enhanced_dyscalculia_solution',
    'provide_improved_dyscalculia_solution',
    'provide_tdah_solution'
]