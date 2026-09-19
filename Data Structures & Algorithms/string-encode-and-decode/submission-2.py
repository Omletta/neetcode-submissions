class Solution:
    
    def encode(self, strs: List[str]) -> str:
        
        coded_word = ''
        for word in strs : 
            coded_word += '#' + str(len(word))+ word 
            print(coded_word)
        return coded_word



    def decode(self, s: str) -> List[str]:


        separated_words = []
        for i in range(0,len(s)) :

            decoded_word= ''
            print(s[i])
            
            if s[i] =='#' and len(s) != 1:
                
                for j in range(i+2,i + int(s[i+1])+2):  
                    decoded_word += s[j]
                    

                separated_words.append(decoded_word)

            elif s[i] =='#' and len(s) == 1:
                return ['#']

        return separated_words

        