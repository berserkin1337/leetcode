class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD =  10**9 + 7
        @cache
        def  StringsStartingWith(c,N):
            if N == 1:
                return 1 
            match c:
                case 'a':
                    return (StringsStartingWith('e', N-1) % MOD)
                case 'e':
                    return (StringsStartingWith('a', N - 1) + StringsStartingWith('i', N - 1)) % MOD
                case 'i' :
                    return (StringsStartingWith('a', N - 1) + StringsStartingWith('e', N - 1) +  StringsStartingWith('o', N - 1) + StringsStartingWith('u', N - 1)) % MOD
                case 'o' :
                    return (StringsStartingWith('i', N - 1) + StringsStartingWith('u', N - 1)) %MOD
                case 'u' :
                    return StringsStartingWith('a', N - 1) % MOD
            print("ILLEGAL  CHAR DETECTED")
            return -1
        
        return (StringsStartingWith('a',n) + StringsStartingWith('e', n) + StringsStartingWith('i',n) + StringsStartingWith('o', n ) + StringsStartingWith('u' , n)) % MOD