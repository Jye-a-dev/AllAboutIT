# ==========================================
# 0. ROOT EXISTING FUNCTIONS (Cộng danh sách)
# ==========================================
from Python.Basic.Types.List.Plus2List import add_lists
from Python.Basic.Types.List.PlusNList import plus_lists

# ==========================================
# 1. LIST PROPERTIES (Kiểm tra tính chất)
# ==========================================
from Python.Basic.Types.List.Properties.CheckEmptyList import is_Empty_List
from Python.Basic.Types.List.Properties.CheckSortedAscending import is_Sorted_Ascending
from Python.Basic.Types.List.Properties.CheckSortedDescending import is_Sorted_Descending
from Python.Basic.Types.List.Properties.CheckAllUnique import is_All_Unique
from Python.Basic.Types.List.Properties.CheckPalindromeList import is_Palindrome_List
from Python.Basic.Types.List.Properties.CheckEqualLists import is_Equal_Lists
from Python.Basic.Types.List.Properties.CheckSubsetList import is_Subset_List
from Python.Basic.Types.List.Properties.CheckDisjointLists import is_Disjoint_Lists
from Python.Basic.Types.List.Properties.CheckAllNumericList import is_All_Numeric_List

# ==========================================
# 2. LIST MEASUREMENT (Đo lường, đếm & tần suất)
# ==========================================
from Python.Basic.Types.List.Measurement.CountListLength import count_List_Length
from Python.Basic.Types.List.Measurement.CountElementOccurrences import count_Element_Occurrences
from Python.Basic.Types.List.Measurement.CountUniqueElements import count_Unique_Elements
from Python.Basic.Types.List.Measurement.CountTruthyElements import count_Truthy_Elements
from Python.Basic.Types.List.Measurement.CountFalsyElements import count_Falsy_Elements
from Python.Basic.Types.List.Measurement.CountFrequencyDict import count_Frequency_Dict
from Python.Basic.Types.List.Measurement.MostFrequentElement import find_Most_Frequent
from Python.Basic.Types.List.Measurement.LeastFrequentElement import find_Least_Frequent

# ==========================================
# 3. LIST MANIPULATION (Thêm, xóa, sửa & biến đổi)
# ==========================================
from Python.Basic.Types.List.Manipulation.AppendElement import append_Element
from Python.Basic.Types.List.Manipulation.PrependElement import prepend_Element
from Python.Basic.Types.List.Manipulation.InsertElementAt import insert_Element_At
from Python.Basic.Types.List.Manipulation.RemoveElementValue import remove_Element_Value
from Python.Basic.Types.List.Manipulation.RemoveAllOccurrences import remove_All_Occurrences
from Python.Basic.Types.List.Manipulation.RemoveAtIndex import remove_At_Index
from Python.Basic.Types.List.Manipulation.ReplaceElementValue import replace_Element_Value
from Python.Basic.Types.List.Manipulation.RemoveDuplicateElements import remove_Duplicate_Elements
from Python.Basic.Types.List.Manipulation.RemoveFalsyValues import remove_Falsy_Values
from Python.Basic.Types.List.Manipulation.ReverseList import reverse_List
from Python.Basic.Types.List.Manipulation.RotateLeftList import rotate_Left_List
from Python.Basic.Types.List.Manipulation.RotateRightList import rotate_Right_List
from Python.Basic.Types.List.Manipulation.ShuffleList import shuffle_List

# ==========================================
# 4. SLICING & PARTITION (Cắt, chia nhóm & làm phẳng)
# ==========================================
from Python.Basic.Types.List.SlicingAndPartition.GetFirstElement import get_First_Element
from Python.Basic.Types.List.SlicingAndPartition.GetLastElement import get_Last_Element
from Python.Basic.Types.List.SlicingAndPartition.GetNthElement import get_Nth_Element
from Python.Basic.Types.List.SlicingAndPartition.SliceList import slice_List
from Python.Basic.Types.List.SlicingAndPartition.TakeFirstN import take_First_N
from Python.Basic.Types.List.SlicingAndPartition.DropFirstN import drop_First_N
from Python.Basic.Types.List.SlicingAndPartition.ChunkList import chunk_List
from Python.Basic.Types.List.SlicingAndPartition.PartitionByCondition import partition_Even_Odd
from Python.Basic.Types.List.SlicingAndPartition.FlattenShallowList import flatten_Shallow_List
from Python.Basic.Types.List.SlicingAndPartition.FlattenDeepList import flatten_Deep_List

# ==========================================
# 5. SEARCH & FILTER (Tìm kiếm & Lọc phần tử)
# ==========================================
from Python.Basic.Types.List.SearchAndFilter.ContainsElement import contains_Element
from Python.Basic.Types.List.SearchAndFilter.FindFirstIndexList import find_First_Index_List
from Python.Basic.Types.List.SearchAndFilter.FindLastIndexList import find_Last_Index_List
from Python.Basic.Types.List.SearchAndFilter.FindAllIndicesList import find_All_Indices_List
from Python.Basic.Types.List.SearchAndFilter.FilterEvenNumbers import filter_Even_Numbers
from Python.Basic.Types.List.SearchAndFilter.FilterOddNumbers import filter_Odd_Numbers
from Python.Basic.Types.List.SearchAndFilter.FilterPositiveNumbers import filter_Positive_Numbers
from Python.Basic.Types.List.SearchAndFilter.FilterNegativeNumbers import filter_Negative_Numbers
from Python.Basic.Types.List.SearchAndFilter.FilterInRange import filter_In_Range

# ==========================================
# 6. SORTING & SET OPERATIONS (Sắp xếp & Phép toán tập hợp)
# ==========================================
from Python.Basic.Types.List.SortingAndSetOps.SortAscending import sort_Ascending
from Python.Basic.Types.List.SortingAndSetOps.SortDescending import sort_Descending
from Python.Basic.Types.List.SortingAndSetOps.SortByStringLength import sort_By_String_Length
from Python.Basic.Types.List.SortingAndSetOps.Union2Lists import union_2_Lists
from Python.Basic.Types.List.SortingAndSetOps.Intersection2Lists import intersection_2_Lists
from Python.Basic.Types.List.SortingAndSetOps.Difference2Lists import difference_2_Lists
from Python.Basic.Types.List.SortingAndSetOps.SymmetricDifferenceLists import symmetric_Difference_Lists
from Python.Basic.Types.List.SortingAndSetOps.Zip2Lists import zip_2_Lists
from Python.Basic.Types.List.SortingAndSetOps.CartesianProductLists import cartesian_Product_Lists

# ==========================================
# 7. LIST STATISTICS (Thống kê danh sách số)
# ==========================================
from Python.Basic.Types.List.Statistics.SumListElements import sum_List_Elements
from Python.Basic.Types.List.Statistics.ProductListElements import product_List_Elements
from Python.Basic.Types.List.Statistics.MeanListElements import mean_List_Elements
from Python.Basic.Types.List.Statistics.MedianListElements import median_List_Elements
from Python.Basic.Types.List.Statistics.VarianceListElements import variance_List_Elements
from Python.Basic.Types.List.Statistics.StdDevListElements import std_Dev_List_Elements
from Python.Basic.Types.List.Statistics.MaxListElement import max_List_Element
from Python.Basic.Types.List.Statistics.MinListElement import min_List_Element
from Python.Basic.Types.List.Statistics.SecondLargestElement import find_Second_Largest
from Python.Basic.Types.List.Statistics.SecondSmallestElement import find_Second_Smallest
from Python.Basic.Types.List.Statistics.CumulativeSumList import cumulative_Sum_List

# ==========================================
# EXPORTS
# ==========================================
__all__ = [
    name
    for name, value in globals().items()
    if not name.startswith("_") and callable(value)
]
