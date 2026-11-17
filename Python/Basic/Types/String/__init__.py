# ==========================================
# 1. STRING PROPERTIES (Kiểm tra tính chất)
# ==========================================
from Python.Basic.Types.String.Properties.CheckEmptyString import is_Empty
from Python.Basic.Types.String.Properties.CheckPalindromeString import is_Palindrome
from Python.Basic.Types.String.Properties.CheckAnagram import is_Anagram
from Python.Basic.Types.String.Properties.CheckIsogram import is_Isogram
from Python.Basic.Types.String.Properties.CheckPangram import is_Pangram
from Python.Basic.Types.String.Properties.CheckAlpha import is_Alpha
from Python.Basic.Types.String.Properties.CheckNumeric import is_Numeric
from Python.Basic.Types.String.Properties.CheckAlphanumeric import is_Alphanumeric
from Python.Basic.Types.String.Properties.CheckUppercase import is_Uppercase
from Python.Basic.Types.String.Properties.CheckLowercase import is_Lowercase
from Python.Basic.Types.String.Properties.CheckTitlecase import is_Titlecase
from Python.Basic.Types.String.Properties.CheckIdentifier import is_Valid_Identifier
from Python.Basic.Types.String.Properties.CheckEmail import is_Valid_Email
from Python.Basic.Types.String.Properties.CheckUrl import is_Valid_Url
from Python.Basic.Types.String.Properties.CheckIpv4 import is_Valid_Ipv4

# ==========================================
# 2. STRING MEASUREMENT (Đếm & Đo lường)
# ==========================================
from Python.Basic.Types.String.Measurement.CountLength import count_Length
from Python.Basic.Types.String.Measurement.CountWords import count_Words
from Python.Basic.Types.String.Measurement.CountVowels import count_Vowels
from Python.Basic.Types.String.Measurement.CountConsonants import count_Consonants
from Python.Basic.Types.String.Measurement.CountDigitsInString import count_Digits
from Python.Basic.Types.String.Measurement.CountUppercase import count_Uppercase
from Python.Basic.Types.String.Measurement.CountLowercase import count_Lowercase
from Python.Basic.Types.String.Measurement.CountSpaces import count_Spaces
from Python.Basic.Types.String.Measurement.CountSpecialChars import count_Special_Chars
from Python.Basic.Types.String.Measurement.CountSubstring import count_Substring
from Python.Basic.Types.String.Measurement.CountCharFrequency import count_Char_Frequency

# ==========================================
# 3. CASE CONVERSION (Chuyển đổi kiểu chữ)
# ==========================================
from Python.Basic.Types.String.CaseConversion.ToUppercase import to_Uppercase
from Python.Basic.Types.String.CaseConversion.ToLowercase import to_Lowercase
from Python.Basic.Types.String.CaseConversion.ToTitlecase import to_Titlecase
from Python.Basic.Types.String.CaseConversion.ToSentenceCase import to_Sentence_Case
from Python.Basic.Types.String.CaseConversion.SwapCase import swap_Case
from Python.Basic.Types.String.CaseConversion.ToCamelCase import to_Camel_Case
from Python.Basic.Types.String.CaseConversion.ToPascalCase import to_Pascal_Case
from Python.Basic.Types.String.CaseConversion.ToSnakeCase import to_Snake_Case
from Python.Basic.Types.String.CaseConversion.ToKebabCase import to_Kebab_Case
from Python.Basic.Types.String.CaseConversion.ToSlug import to_Slug

# ==========================================
# 4. STRING MANIPULATION (Thao tác chuỗi)
# ==========================================
from Python.Basic.Types.String.Manipulation.ReverseString import reverse_String
from Python.Basic.Types.String.Manipulation.ReverseWords import reverse_Words
from Python.Basic.Types.String.Manipulation.Concat2Strings import concat_2_Strings
from Python.Basic.Types.String.Manipulation.ConcatNStrings import concat_N_Strings
from Python.Basic.Types.String.Manipulation.RepeatString import repeat_String
from Python.Basic.Types.String.Manipulation.InsertSubstring import insert_Substring
from Python.Basic.Types.String.Manipulation.RemoveSubstring import remove_Substring
from Python.Basic.Types.String.Manipulation.ReplaceSubstring import replace_Substring
from Python.Basic.Types.String.Manipulation.RemoveDuplicates import remove_Duplicate_Chars
from Python.Basic.Types.String.Manipulation.RemoveVowels import remove_Vowels
from Python.Basic.Types.String.Manipulation.RemovePunctuation import remove_Punctuation
from Python.Basic.Types.String.Manipulation.RemoveAccents import remove_Accents

# ==========================================
# 5. TRIM & PAD (Cắt tỉa & Đệm chuỗi)
# ==========================================
from Python.Basic.Types.String.TrimAndPad.TrimString import trim_String
from Python.Basic.Types.String.TrimAndPad.TrimLeft import trim_Left
from Python.Basic.Types.String.TrimAndPad.TrimRight import trim_Right
from Python.Basic.Types.String.TrimAndPad.NormalizeSpaces import normalize_Spaces
from Python.Basic.Types.String.TrimAndPad.PadLeft import pad_Left
from Python.Basic.Types.String.TrimAndPad.PadRight import pad_Right
from Python.Basic.Types.String.TrimAndPad.CenterString import center_String
from Python.Basic.Types.String.TrimAndPad.TruncateString import truncate_String

# ==========================================
# 6. SPLIT & JOIN (Tách & Ghép chuỗi)
# ==========================================
from Python.Basic.Types.String.SplitAndJoin.SplitByDelimiter import split_By_Delimiter
from Python.Basic.Types.String.SplitAndJoin.SplitWords import split_Words
from Python.Basic.Types.String.SplitAndJoin.SplitLines import split_Lines
from Python.Basic.Types.String.SplitAndJoin.SplitChunks import split_Chunks
from Python.Basic.Types.String.SplitAndJoin.JoinStrings import join_Strings

# ==========================================
# 7. SEARCH & EXTRACT (Tìm kiếm & Trích xuất)
# ==========================================
from Python.Basic.Types.String.SearchAndExtract.ContainsSubstring import contains_Substring
from Python.Basic.Types.String.SearchAndExtract.StartsWith import starts_With
from Python.Basic.Types.String.SearchAndExtract.EndsWith import ends_With
from Python.Basic.Types.String.SearchAndExtract.FindFirstIndex import find_First_Index
from Python.Basic.Types.String.SearchAndExtract.FindLastIndex import find_Last_Index
from Python.Basic.Types.String.SearchAndExtract.FindAllIndices import find_All_Indices
from Python.Basic.Types.String.SearchAndExtract.ExtractDigits import extract_Digits
from Python.Basic.Types.String.SearchAndExtract.ExtractLetters import extract_Letters
from Python.Basic.Types.String.SearchAndExtract.ExtractEmails import extract_Emails
from Python.Basic.Types.String.SearchAndExtract.ExtractUrls import extract_Urls
from Python.Basic.Types.String.SearchAndExtract.LongestWord import find_Longest_Word
from Python.Basic.Types.String.SearchAndExtract.ShortestWord import find_Shortest_Word

# ==========================================
# 8. COMPARISON & SIMILARITY (So sánh & Tương đồng)
# ==========================================
from Python.Basic.Types.String.ComparisonAndSimilarity.CompareStrings import compare_Strings
from Python.Basic.Types.String.ComparisonAndSimilarity.LongestCommonPrefix import longest_Common_Prefix
from Python.Basic.Types.String.ComparisonAndSimilarity.LongestCommonSuffix import longest_Common_Suffix
from Python.Basic.Types.String.ComparisonAndSimilarity.LevenshteinDistance import levenshtein_Distance
from Python.Basic.Types.String.ComparisonAndSimilarity.HammingDistance import hamming_Distance

# ==========================================
# 9. ENCODING & CONVERSION (Mã hóa & Chuyển đổi)
# ==========================================
from Python.Basic.Types.String.EncodingAndConversion.StringToAscii import to_Ascii_List
from Python.Basic.Types.String.EncodingAndConversion.AsciiToString import from_Ascii_List
from Python.Basic.Types.String.EncodingAndConversion.StringToBinary import to_Binary_String
from Python.Basic.Types.String.EncodingAndConversion.BinaryToString import from_Binary_String
from Python.Basic.Types.String.EncodingAndConversion.StringToHex import to_Hex_String
from Python.Basic.Types.String.EncodingAndConversion.HexToString import from_Hex_String
from Python.Basic.Types.String.EncodingAndConversion.StringToBase64 import to_Base64
from Python.Basic.Types.String.EncodingAndConversion.Base64ToString import from_Base64
from Python.Basic.Types.String.EncodingAndConversion.StringToMorse import to_Morse_String
from Python.Basic.Types.String.EncodingAndConversion.MorseToString import from_Morse_String
from Python.Basic.Types.String.EncodingAndConversion.CaesarCipher import caesar_Cipher
from Python.Basic.Types.String.EncodingAndConversion.RunLengthEncode import run_Length_Encode
from Python.Basic.Types.String.EncodingAndConversion.RunLengthDecode import run_Length_Decode

# ==========================================
# EXPORTS
# ==========================================
__all__ = [
    name
    for name, value in globals().items()
    if not name.startswith("_") and callable(value)
]
