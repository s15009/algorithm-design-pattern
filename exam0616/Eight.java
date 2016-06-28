import static java.lang.System.out;
class Queen {
    int queen = 8;
    int queenpos[] = new int [queen];
    int queencount = 0;
    boolean [][] Bord = new boolean [queen][queen];
    boolean [] row = new boolean [queen];
    boolean [] col = new boolean [queen];
    boolean [] pos = new boolean [queen * 2 - 1];
    boolean [] neg = new boolean [queen * 2 - 1];

    boolean safe = false;
    boolean out = true;
    public void makeinit(){
        //Falseをセット
        for(int i = 0;i < queen;i++){
            for(int l = 0;l < queen;l++){
                Bord[i][l] = false;
            }
        }
    }
    public void setqueen(int i){
        for(int l = 0;l < queen;l++){
            if(!isjudge(l, i)){
                Bord[i][l] = out;
                if(i == (queen - 1)){
                    queencount++;
                    //System.out.printf("%s\n",(Bord[i][l] ? "Q" : "-"));
                    bordprint();
                    System.out.println(queencount);
                }
                else{
                    setjudge(l, i, out);
                    //bordprint();
                    setqueen(i + 1);
                    //setjudge(l, i, safe);
                }
            setjudge(l, i, safe);
            }
        }
    }
    public void setjudge(int x, int y, boolean flag){
        row[y] = flag;
        col[x] = flag;
        pos[x + y] = flag;
        neg[y - x + (queen - 1)] = flag;
        Bord[y][x] = flag;
    }
    public boolean isjudge(int x, int y){
        if(row[y] || col[x] || pos[x + y] || neg[y - x + (queen - 1)]){
            return true;
        }
        else {
            return false;
        }

    }
    public void bordprint(){
        for(int i = 0;i < queen;i++){
            for(int l = 0;l < queen;l++){
                if(Bord[i][l]){
                    System.out.print("Q");
                }
                else{
                    System.out.print("-");
                }
            }
            System.out.println("");
        }
    }



}

public class Eight{
    public static void main(String...args){
        Queen qu = new Queen();
        qu.makeinit();
        qu.setqueen(0);
    }
}
