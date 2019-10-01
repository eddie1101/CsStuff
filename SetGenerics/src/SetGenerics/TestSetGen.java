package SetGenerics;

public class TestSetGen {
    public static void main(String[] args) {
        SetGen<String> set1 = new SetGen<String>();
        SetGen<String> set2 = new SetGen<String>();

        set1.add("Banana");
        set1.add("Banana");
        set1.add("Apple");
        set1.add("Orange");
        set1.add("Peach");
        set1.add("Plum");

        set2.add("Blueberry");
        set2.add("Citrine");
        set2.add("Dragonfruit");
        set2.add("Watermelon");
        set2.add("Plum");

        System.out.println(set1.getUnion(set2));
        System.out.println(set1.getSet());
        System.out.println(set2.getSet());
        System.out.println(set1.getDifference(set2));
    }
}
