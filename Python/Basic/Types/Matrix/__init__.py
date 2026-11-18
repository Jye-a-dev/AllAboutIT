# ==========================================
# 0. ROOT EXISTING FUNCTIONS (Cộng ma trận)
# ==========================================
from Python.Basic.Types.Matrix.Arithmetic.Plus2Matrix import add_matrices, add_2_Matrices
from Python.Basic.Types.Matrix.Arithmetic.PlusNMatrix import plus_Matries, plus_matrices, add_N_Matrices

# ==========================================
# 1. MATRIX PROPERTIES (Kiểm tra tính chất)
# ==========================================
from Python.Basic.Types.Matrix.Properties.CheckEmptyMatrix import is_Empty_Matrix
from Python.Basic.Types.Matrix.Properties.CheckSquareMatrix import is_Square_Matrix
from Python.Basic.Types.Matrix.Properties.CheckZeroMatrix import is_Zero_Matrix
from Python.Basic.Types.Matrix.Properties.CheckIdentityMatrix import is_Identity_Matrix
from Python.Basic.Types.Matrix.Properties.CheckDiagonalMatrix import is_Diagonal_Matrix
from Python.Basic.Types.Matrix.Properties.CheckScalarMatrix import is_Scalar_Matrix
from Python.Basic.Types.Matrix.Properties.CheckUpperTriangular import is_Upper_Triangular
from Python.Basic.Types.Matrix.Properties.CheckLowerTriangular import is_Lower_Triangular
from Python.Basic.Types.Matrix.Properties.CheckSymmetricMatrix import is_Symmetric_Matrix
from Python.Basic.Types.Matrix.Properties.CheckSkewSymmetric import is_Skew_Symmetric
from Python.Basic.Types.Matrix.Properties.CheckSingularMatrix import is_Singular_Matrix
from Python.Basic.Types.Matrix.Properties.CheckOrthogonalMatrix import is_Orthogonal_Matrix
from Python.Basic.Types.Matrix.Properties.CheckEqualMatrices import is_Equal_Matrices
from Python.Basic.Types.Matrix.Properties.CheckSameShape import is_Same_Shape

# ==========================================
# 2. MATRIX MEASUREMENT (Kích thước, định thức & chuẩn)
# ==========================================
from Python.Basic.Types.Matrix.Measurement.GetShape import get_Matrix_Shape
from Python.Basic.Types.Matrix.Measurement.CountRows import count_Rows
from Python.Basic.Types.Matrix.Measurement.CountColumns import count_Columns
from Python.Basic.Types.Matrix.Measurement.CountTotalElements import count_Total_Elements
from Python.Basic.Types.Matrix.Measurement.CountZeroElements import count_Zero_Elements
from Python.Basic.Types.Matrix.Measurement.CountNonZeroElements import count_Non_Zero_Elements
from Python.Basic.Types.Matrix.Measurement.TraceMatrix import trace_Matrix
from Python.Basic.Types.Matrix.Measurement.Determinant2x2 import determinant_2x2
from Python.Basic.Types.Matrix.Measurement.Determinant3x3 import determinant_3x3
from Python.Basic.Types.Matrix.Measurement.DeterminantNxN import determinant_NxN
from Python.Basic.Types.Matrix.Measurement.RankMatrix import rank_Matrix
from Python.Basic.Types.Matrix.Measurement.FrobeniusNorm import frobenius_Norm

# ==========================================
# 3. MATRIX ARITHMETIC (Phép toán đại số ma trận)
# ==========================================
from Python.Basic.Types.Matrix.Arithmetic.Subtract2Matrices import subtract_2_Matrices
from Python.Basic.Types.Matrix.Arithmetic.SubtractNMatrices import subtract_N_Matrices
from Python.Basic.Types.Matrix.Arithmetic.Multiply2Matrices import multiply_2_Matrices
from Python.Basic.Types.Matrix.Arithmetic.MultiplyNMatrices import multiply_N_Matrices
from Python.Basic.Types.Matrix.Arithmetic.ScalarMultiplyMatrix import scalar_Multiply_Matrix
from Python.Basic.Types.Matrix.Arithmetic.ScalarDivideMatrix import scalar_Divide_Matrix
from Python.Basic.Types.Matrix.Arithmetic.NegateMatrix import negate_Matrix
from Python.Basic.Types.Matrix.Arithmetic.HadamardProductMatrix import hadamard_Product_Matrix
from Python.Basic.Types.Matrix.Arithmetic.HadamardDivideMatrix import hadamard_Divide_Matrix
from Python.Basic.Types.Matrix.Arithmetic.PowerMatrix import power_Matrix

# ==========================================
# 4. LINEAR ALGEBRA (Đại số tuyến tính & Biến đổi)
# ==========================================
from Python.Basic.Types.Matrix.LinearAlgebra.TransposeMatrix import transpose_Matrix
from Python.Basic.Types.Matrix.LinearAlgebra.MinorMatrix import minor_Matrix
from Python.Basic.Types.Matrix.LinearAlgebra.CofactorMatrix import cofactor_Matrix
from Python.Basic.Types.Matrix.LinearAlgebra.AdjugateMatrix import adjugate_Matrix
from Python.Basic.Types.Matrix.LinearAlgebra.Inverse2x2 import inverse_2x2
from Python.Basic.Types.Matrix.LinearAlgebra.InverseNxN import inverse_NxN
from Python.Basic.Types.Matrix.LinearAlgebra.RowEchelonForm import to_Row_Echelon_Form
from Python.Basic.Types.Matrix.LinearAlgebra.ReducedRowEchelon import to_Reduced_Row_Echelon_Form

# ==========================================
# 5. CREATION & MANIPULATION (Khởi tạo & Thao tác)
# ==========================================
from Python.Basic.Types.Matrix.CreationAndManipulation.CreateZeroMatrix import create_Zero_Matrix
from Python.Basic.Types.Matrix.CreationAndManipulation.CreateOnesMatrix import create_Ones_Matrix
from Python.Basic.Types.Matrix.CreationAndManipulation.CreateIdentityMatrix import create_Identity_Matrix
from Python.Basic.Types.Matrix.CreationAndManipulation.CreateDiagonalMatrix import create_Diagonal_Matrix
from Python.Basic.Types.Matrix.CreationAndManipulation.GetRow import get_Row
from Python.Basic.Types.Matrix.CreationAndManipulation.GetColumn import get_Column
from Python.Basic.Types.Matrix.CreationAndManipulation.GetMainDiagonal import get_Main_Diagonal
from Python.Basic.Types.Matrix.CreationAndManipulation.GetAntiDiagonal import get_Anti_Diagonal
from Python.Basic.Types.Matrix.CreationAndManipulation.FlattenMatrix import flatten_Matrix
from Python.Basic.Types.Matrix.CreationAndManipulation.ReshapeMatrix import reshape_Matrix
from Python.Basic.Types.Matrix.CreationAndManipulation.Submatrix import extract_Submatrix
from Python.Basic.Types.Matrix.CreationAndManipulation.ConcatHorizontal import concat_Horizontal
from Python.Basic.Types.Matrix.CreationAndManipulation.ConcatVertical import concat_Vertical

# ==========================================
# 6. GEOMETRIC TRANSFORM (Lật & Xoay)
# ==========================================
from Python.Basic.Types.Matrix.GeometricTransform.FlipHorizontal import flip_Horizontal
from Python.Basic.Types.Matrix.GeometricTransform.FlipVertical import flip_Vertical
from Python.Basic.Types.Matrix.GeometricTransform.Rotate90Clockwise import rotate_90_Clockwise
from Python.Basic.Types.Matrix.GeometricTransform.Rotate90CounterClockwise import rotate_90_Counter_Clockwise
from Python.Basic.Types.Matrix.GeometricTransform.Rotate180 import rotate_180
from Python.Basic.Types.Matrix.GeometricTransform.SwapRows import swap_Rows
from Python.Basic.Types.Matrix.GeometricTransform.SwapColumns import swap_Columns

# ==========================================
# 7. STATISTICS (Thống kê ma trận)
# ==========================================
from Python.Basic.Types.Matrix.Statistics.SumAllElements import sum_All_Elements
from Python.Basic.Types.Matrix.Statistics.SumRows import sum_Rows
from Python.Basic.Types.Matrix.Statistics.SumColumns import sum_Columns
from Python.Basic.Types.Matrix.Statistics.MeanAllElements import mean_All_Elements
from Python.Basic.Types.Matrix.Statistics.MaxElementMatrix import max_Element_Matrix
from Python.Basic.Types.Matrix.Statistics.MinElementMatrix import min_Element_Matrix
from Python.Basic.Types.Matrix.Statistics.MaxInRows import max_In_Rows
from Python.Basic.Types.Matrix.Statistics.MinInRows import min_In_Rows
from Python.Basic.Types.Matrix.Statistics.MaxInColumns import max_In_Columns
from Python.Basic.Types.Matrix.Statistics.MinInColumns import min_In_Columns

# ==========================================
# EXPORTS
# ==========================================
__all__ = [
    name
    for name, value in globals().items()
    if not name.startswith("_") and callable(value)
]
