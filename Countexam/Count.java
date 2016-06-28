import static java.lang.System.out;
public class Count {
    public static void main(String...args){
        Sfmt sfmt = new Sfmt(256);

        //ビットカウント　タイム越したいやつ
        long start = System.currentTimeMillis();

        for(int l = 0;l < 1000000;l++){
            for(int i = 0; i <= 256;i++){
                int num = (byte)sfmt.NextInt(256);
                int ans = Integer.bitCount(num);
            }
        }
        long end = System.currentTimeMillis();
        out.printf("bitCount奴wwwwwwww: %.4f\n", (double)(end - start) / 1000);


        //2で割り続けるやつ
        start = System.currentTimeMillis();
        for(int p = 0;p < 1000000;p++){
            int i = 0;
            while(i <= 256){
                int count = 0;
                int num = (byte)sfmt.NextInt(256);
                //out.print(num + " ");
                while(num != 0){
                    count += num % 2;
                    num /= 2;
                }
                //out.println(count);
                i++;
            }
        }
        end = System.currentTimeMillis();
        out.printf("2while: %.4f\n", (double)(end - start) / 1000);


        //binarystringで配列にして比較していく
        start = System.currentTimeMillis();
        for(int x = 0;x < 1000000;x++){
            for(int a = 0; a < 256;a++){
                int c = 0;
                int b = (byte)sfmt.NextInt(256);
                String Binary = Integer.toBinaryString(b);
                char target = '1';
                //char[] ch = Binary.toCharArray();
                for(char value: Binary.toCharArray()){
                    if(value == target){
                        c++;
                    }
                }
                //out.println(b + "の1の個数は" + c);
            }
        }
        end = System.currentTimeMillis();
        out.printf("charfor: %.4f\n", (double)(end - start) / 1000);



        start = System.currentTimeMillis();
        for(int y = 0;y < 1000000;y++){
            for(int j = 0;j < 256;j++){
                int b = (byte)sfmt.NextInt(256);
                int count = 0;
                String Binary = Integer.toBinaryString(b);
                String[] tmp =  Binary.split("");
                for(String value: tmp){
                    int i = Integer.parseInt(value);
                    count += i;
                }
                //out.println(count);

            }
        }
        end = System.currentTimeMillis();
        out.printf("sumfor: %.4f\n", (double)(end - start) / 1000);

    }
}

