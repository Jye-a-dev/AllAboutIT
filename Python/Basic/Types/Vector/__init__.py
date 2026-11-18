# ==========================================
# 0. ROOT EXISTING FUNCTIONS (Cộng vector)
# ==========================================
from Python.Basic.Types.Vector.Arithmetic.Plus2Vector import add_2_Vectors, add_vectors
from Python.Basic.Types.Vector.Arithmetic.PlusNVector import add_N_Vectors, plus_vectors

# ==========================================
# 1. VECTOR PROPERTIES (Kiểm tra tính chất)
# ==========================================
from Python.Basic.Types.Vector.Properties.CheckZeroVector import is_Zero_Vector
from Python.Basic.Types.Vector.Properties.CheckUnitVector import is_Unit_Vector
from Python.Basic.Types.Vector.Properties.CheckEqualVectors import is_Equal_Vectors
from Python.Basic.Types.Vector.Properties.CheckSameDimension import is_Same_Dimension
from Python.Basic.Types.Vector.Properties.CheckOrthogonal import is_Orthogonal
from Python.Basic.Types.Vector.Properties.CheckParallel import is_Parallel

# ==========================================
# 2. VECTOR MEASUREMENT (Độ lớn & Khoảng cách)
# ==========================================
from Python.Basic.Types.Vector.Measurement.VectorDimension import get_Dimension
from Python.Basic.Types.Vector.Measurement.MagnitudeL2 import magnitude_L2
from Python.Basic.Types.Vector.Measurement.MagnitudeL1 import magnitude_L1
from Python.Basic.Types.Vector.Measurement.MagnitudeLInf import magnitude_L_Inf
from Python.Basic.Types.Vector.Measurement.EuclideanDistance import euclidean_Distance
from Python.Basic.Types.Vector.Measurement.ManhattanDistance import manhattan_Distance
from Python.Basic.Types.Vector.Measurement.ChebyshevDistance import chebyshev_Distance
from Python.Basic.Types.Vector.Measurement.MinkowskiDistance import minkowski_Distance
from Python.Basic.Types.Vector.Measurement.HammingDistanceVector import hamming_Distance_Vector

# ==========================================
# 3. VECTOR ARITHMETIC (Phép toán số học)
# ==========================================
from Python.Basic.Types.Vector.Arithmetic.Subtract2Vectors import subtract_2_Vectors
from Python.Basic.Types.Vector.Arithmetic.SubtractNVectors import subtract_N_Vectors
from Python.Basic.Types.Vector.Arithmetic.ScalarMultiply import scalar_Multiply
from Python.Basic.Types.Vector.Arithmetic.ScalarDivide import scalar_Divide
from Python.Basic.Types.Vector.Arithmetic.NegateVector import negate_Vector
from Python.Basic.Types.Vector.Arithmetic.HadamardProduct import hadamard_Product
from Python.Basic.Types.Vector.Arithmetic.HadamardDivide import hadamard_Divide

# ==========================================
# 4. PRODUCTS & ANGLES (Tích & Góc)
# ==========================================
from Python.Basic.Types.Vector.ProductsAndAngles.DotProduct import dot_Product
from Python.Basic.Types.Vector.ProductsAndAngles.CrossProduct2D import cross_Product_2D
from Python.Basic.Types.Vector.ProductsAndAngles.CrossProduct3D import cross_Product_3D
from Python.Basic.Types.Vector.ProductsAndAngles.ScalarTripleProduct import scalar_Triple_Product
from Python.Basic.Types.Vector.ProductsAndAngles.AngleRadians import angle_Between_Radians
from Python.Basic.Types.Vector.ProductsAndAngles.AngleDegrees import angle_Between_Degrees
from Python.Basic.Types.Vector.ProductsAndAngles.CosineSimilarity import cosine_Similarity

# ==========================================
# 5. TRANSFORMATION (Biến đổi & Chiếu)
# ==========================================
from Python.Basic.Types.Vector.Transformation.NormalizeVector import normalize_Vector
from Python.Basic.Types.Vector.Transformation.ProjectVector import project_Vector
from Python.Basic.Types.Vector.Transformation.RejectVector import reject_Vector
from Python.Basic.Types.Vector.Transformation.ReflectVector import reflect_Vector
from Python.Basic.Types.Vector.Transformation.RotateVector2D import rotate_Vector_2D
from Python.Basic.Types.Vector.Transformation.LerpVectors import lerp_Vectors
from Python.Basic.Types.Vector.Transformation.ClampVector import clamp_Vector

# ==========================================
# 6. CREATION & MANIPULATION (Khởi tạo & Thao tác)
# ==========================================
from Python.Basic.Types.Vector.CreationAndManipulation.CreateZeroVector import create_Zero_Vector
from Python.Basic.Types.Vector.CreationAndManipulation.CreateOnesVector import create_Ones_Vector
from Python.Basic.Types.Vector.CreationAndManipulation.CreateBasisVector import create_Basis_Vector
from Python.Basic.Types.Vector.CreationAndManipulation.ReverseVector import reverse_Vector
from Python.Basic.Types.Vector.CreationAndManipulation.ConcatVectors import concat_Vectors
from Python.Basic.Types.Vector.CreationAndManipulation.SliceVector import slice_Vector
from Python.Basic.Types.Vector.CreationAndManipulation.PadVector import pad_Vector

# ==========================================
# 7. STATISTICS (Thống kê phần tử)
# ==========================================
from Python.Basic.Types.Vector.Statistics.SumElements import sum_Vector_Elements
from Python.Basic.Types.Vector.Statistics.MeanElement import mean_Vector_Element
from Python.Basic.Types.Vector.Statistics.MaxElement import max_Vector_Element
from Python.Basic.Types.Vector.Statistics.MinElement import min_Vector_Element
from Python.Basic.Types.Vector.Statistics.ArgMaxVector import argmax_Vector
from Python.Basic.Types.Vector.Statistics.ArgMinVector import argmin_Vector
from Python.Basic.Types.Vector.Statistics.MeanVectors import mean_Vectors

# ==========================================
# EXPORTS
# ==========================================
__all__ = [
    name
    for name, value in globals().items()
    if not name.startswith("_") and callable(value)
]
