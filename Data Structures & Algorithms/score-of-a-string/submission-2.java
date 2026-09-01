class Solution {
    public int scoreOfString(String s) {
        int score = 0;

        for(int i = 0; i<s.length()-1;i++){
            char[] ch = s.toCharArray();
            score += Math.abs(ch[i]-ch[i+1]);
        }
        return score;
    }
}