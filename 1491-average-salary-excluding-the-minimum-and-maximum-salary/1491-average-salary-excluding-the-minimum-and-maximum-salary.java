class Solution {
    public double average(int[] salary) {
        int minSalary = Integer.MAX_VALUE;
        int maxSalary = Integer.MIN_VALUE;
        
        int sum = 0;
        
        for (int money: salary) {
            sum += money;
            minSalary = Math.min(minSalary, money);
            maxSalary = Math.max(maxSalary, money);
            
        }
        return (double)(sum - minSalary - maxSalary) / (double)(salary.length - 2);
        
    }
}