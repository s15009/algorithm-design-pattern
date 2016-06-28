class Primefact {
    private int counter = 0;
    private int a = 2;
    private int inc = 4;
    private int prime1 = 3;
    private int prime2 = 11;
    private int num = 1;
    private int decry = 0;
    private int cons = 0;

    public void calc(int n){
        counter = 0;
        while(n >= a * a){
            if(n % a == 0){
                System.out.printf("%d*", a);
                n /= a;
            }
            else {
                a++;
            }
            counter++;
        }
        System.out.printf("%d\n", n);
        System.out.printf("counter = %d\n", counter);
    }
    public void calc2(int n){
        counter = 0;

        //2check
        a = 2;
        while(n >= a * a){
            if(n % a == 0){
                System.out.printf("%d*", a);
                n /= a;
            }
            else {
                break;
            }
        }
        counter++;

        //3check
        a = 3;
        while(n >= a * a){
            if(n % a == 0){
                System.out.printf("%d*", a);
                n /= a;
            }
            else{
                break;
            }
            counter++;
        }

        //5 Or later and 3 not multiple cut
        a = 5;
        while(n >= a * a){
            if(n % a == 0){
                System.out.printf("%d*", a);
                n /= a;
            }
            else {
                a += (inc ^ 6);
            }
            counter++;
        }
        System.out.printf("%d\n", n);
        System.out.printf("counter = %d\n", counter);
    }

    public void encry (int key, int plain){
        this.num = 1;
        System.out.printf("prime1 = %d\n", prime1);
        System.out.printf("prime2 = %d\n", prime2);
        System.out.printf("key = %d\n", key);
        System.out.printf("plain or chipher = %d\n", plain);

        for(int i = 1;i <= key; i++){
            num *= plain;
        }
        num %= prime1 * prime2;
        System.out.printf("plain or chipher = %d\n", num);
    }
    public int keysearch(int plain){
        cons = 1;
        decry = (cons * (prime1-1) * (prime2-1) + 1) / plain;
        return decry;
    }
    public int getNum(){
        return this.num;
    }
}
public class RSA {
    public static void main(String...args){
        Primefact prfa = new Primefact();
        /*int input = new java.util.Scanner(System.in).nextInt();
        prfa.calc(input);
        prfa.calc2(input);
        */

        System.out.println("適当な数字");
        int key = new java.util.Scanner(System.in).nextInt();
        System.out.println("平文");
        int plain = new java.util.Scanner(System.in).nextInt();
        System.out.println("暗号化");
        prfa.encry(key,plain);
        System.out.println("復号化");
        int key2 = prfa.keysearch(key);
        prfa.encry(key2,prfa.getNum());
    }
}
