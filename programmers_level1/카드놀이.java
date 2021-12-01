import java.util.*;
class Solution {
    public String[] solution(String[] card, String[] word) {
        String[] answer = {};
        List<String> where = new ArrayList<String>();
        String[] array_word;
        for(int i = 0; i<word.length; i++) {
            array_word = word[i].split("");
            boolean flag = true;
            int x = 0;
            int y = 0;
            int z = 0;
            StringBuilder MyString1 = new StringBuilder(card[0]);
            StringBuilder MyString2 = new StringBuilder(card[1]);
            StringBuilder MyString3 = new StringBuilder(card[2]);
            for(int j = 0; j < array_word.length; j++) {
                if (MyString1.indexOf(array_word[j]) != -1) {
                    MyString1 = MyString1.deleteCharAt(MyString1.indexOf(array_word[j]));
                    x=1;
                }
                else if (MyString2.indexOf(array_word[j]) != -1) {
                    MyString2 = MyString2.deleteCharAt(MyString2.indexOf(array_word[j]));
                    y=1;
                }
                else if (MyString3.indexOf(array_word[j]) != -1) {
                    MyString3 = MyString3.deleteCharAt(MyString3.indexOf(array_word[j]));
                    z=1;
                }
                else if (MyString1.indexOf(array_word[j])==-1 && MyString2.indexOf(array_word[j])==-1 && MyString3.indexOf(array_word[j])==-1) {
                    System.out.println(array_word[j]);
                    flag = false;
                }
            }
            if (x==1 && y==1 && z==1 && flag == true) {
                where.add(word[i]);
            }
            
        }
        if (where.size() >= 1) {
            String[] simpleArray = new String[ where.size() ];
            where.toArray( simpleArray );
            return simpleArray;
        }
        else {
            String[] simpleArray = {"-1"};
            return simpleArray;
        }
    }
}