/*
   builder パターン
   produser の指示で
   返すオブジェクト celebrity のフィールドが変化する
*/
interface Builder {
    public void types(String type);
    public void  name(String name);

    public void hobby(String hobby);

    public Object getResult();
}
class Produser {
    private Builder builder;

    Produser(Builder builder){
        this.builder = builder;
    }
    void cuteconstract(){
        builder.name("Uduki");
        builder.types("Cute");
        builder.hobby("long call");

    }
    void coolconstract(){
        builder.name("Rin");
        builder.types("Cool");
        builder.hobby("Dog-walking");

    }

    void passionconstract(){
        builder.name("Kirari");
        builder.types("Passion");
        builder.hobby("cutecorrect");
    }
}

class IdolBuilder implements Builder {
    private Celebrity celebrity;

    IdolBuilder(){
        this.celebrity = new Celebrity();
    }
    @Override
    public void types(String type){
        celebrity.setTypes(type);
    }

    @Override
    public void name(String name){
        celebrity.setName(name);
    }

    @Override
    public void hobby(String hobby){
        celebrity.setHobbby(hobby);
    }

    @Override
    public Object getResult(){
        return celebrity;
    }
}

class Celebrity {
    private String name;
    private String types;
    private String hobby;

    public void setName(String Name){
        this.name = Name;
    }
    public void setTypes(String Type){
        this.types = Type;
    }
    public void setHobbby(String Hobby){
        this.hobby = Hobby;
    }
    @Override
    public String toString(){
        return "名前　" + this.name + "　タイプ　" + this.types + "　趣味　" + this.hobby;
    }
}

// cliant
public class Dereste {
    public static void main(String...args){
        IdolBuilder builder = new IdolBuilder();
        Produser pro = new Produser(builder);
        pro.coolconstract();
        Object get = builder.getResult();
        System.out.println(get);



    }
}
