class Solution {
    public int[] findEvenNumbers(int[] digits) {
        // Đếm tần suất của mỗi chữ số (0-9)
        int[] freq = new int[10];
        for (int digit : digits) {
            freq[digit]++;
        }
        
        // Sử dụng TreeSet để lưu các số hợp lệ duy nhất theo thứ tự sắp xếp
        TreeSet<Integer> treeSet = new TreeSet<>();
        
        // Thử tất cả các tổ hợp có thể cho hàng trăm, hàng chục và hàng đơn vị
        for (int i = 1; i <= 9; i++) { // Hàng trăm (không có số 0 đứng đầu)
            if (freq[i] == 0) continue;
            freq[i]--; // Sử dụng chữ số i
            
            for (int j = 0; j <= 9; j++) { // Hàng chục
                if (freq[j] == 0) continue;
                freq[j]--; // Sử dụng chữ số j
                
                for (int k = 0; k <= 8; k += 2) { // Hàng đơn vị (số chẵn: 0,2,4,6,8)
                    if (freq[k] == 0) continue;
                    // Tạo số
                    int num = i * 100 + j * 10 + k;
                    treeSet.add(num);
                }
                
                freq[j]++; // Khôi phục chữ số j
            }
        /*
        VD cho mang ban dau la [2,2,4]
        freg[2] = 2
        freg[4] = 1
        Voi i = 2
            freg[2] = 2 != 0 
            freg[2] = 1 
            Voi j = 2  
                freg[2] = 1 != 0 
                freg[2] = 0 
                Voi k = 4 
                    Tao so 224 
                Khoi phuc freg[2] = 1 
            Voi j = 4 
                freg[4] = 1 != 0 
                freg[4] = 0 
                Voi k = 2
                    Tao so 242 
                Khoi phuc freg[4] = 1 
            Khoi phuc freg[2] = 2
        */
            freq[i]++; // Khôi phục chữ số i
        }
        
        // Chuyển TreeSet thành mảng
        int[] ans = new int[treeSet.size()];
        int idx = 0;
        for (int num : treeSet) {
            ans[idx++] = num;
        }
        
        return ans;
    }
}