import static java.lang.System.out;
class Greed{
    public void gre(int i){
        int[] val = {500, 100, 50, 10, 5, 1};
        int sum = 0;
        for(int e = 0;e < 6;e++){
            int n = i / val[e];
            out.printf("%d円硬貨 = %d枚\n", val[e], n);
            sum += n;
            i %= val[e];
        }
        out.printf("硬貨の枚数 = %d枚\n", sum);


    }

}
public class Greedy{
    public static void main(String...args){
        out.println("お金をいれてね");
        int money = new java.util.Scanner(System.in).nextInt();
        //out.println(money);
        Greed gr = new Greed();
        gr.gre(money);


    }
}
