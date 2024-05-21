# Type_ahead-

## Introduction
A program called Type_ahead generates auto-suggestions based on a partial input string and a predetermined list of terms. It is frequently used in text editors and search engines to help users finish their words or searches. 


## Apporach
The `type_ahead` Python method is used to implement the auto-suggest feature. Two inputs are received by the function: a partial input string and a list of words. Then, using the incomplete input string as a filter, it searches the list of terms for matches. Depending on whether the input string contains wildcard characters ({'*'}), two matching strategies are used: exact substring matching and wildcard pattern matching. 

- To match the partial input string as a substring precisely, the function builds a regular expression pattern.
For wildcard pattern matching, the function converts the wildcard character (`'*'`) to a regex pattern (`'.*'`) and matches the pattern against each word.

## Testing
The program includes a set of test cases to automate testing using the `unittest` framework. These test cases cover various scenarios, including:
- Exact subword matches
- Wildcard matches
- No matches
- Case-insensitive matches
- Empty input

