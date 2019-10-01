package SetGenerics;
import java.util.ArrayList;

public class SetGen <E>{
    private ArrayList<E> m_list;

    public SetGen(){
        m_list = new ArrayList<E>();
    }

    public ArrayList<E> getSet(){
        return m_list;
    }

    /**
     * If the given element is not the set, add it.
     * @param element The element to add to the set.
     */
    public void add(E element){
        if(!m_list.contains(element)) {
            m_list.add(element);
        }
    }

    /**
     * If the given element is in the set, remove it.
     * @param element The element to remove.
     */
    public void remove(E element){
        if(m_list.contains(element)){
            m_list.remove(element);
        }
    }

    /**
     * Make this set into a union with a given set.
     * @param o The set to union with.
     */
    public void makeUnion(SetGen<E> o){
        for(E element: o.getSet()){
            if(!m_list.contains(element)){
                this.add(element);
            }
        }
    }

    /**
     * Make a new set out of a union with this set and a given set.
     * @param o The given set to union with.
     * @return The new set, which is a union of this set and the given set.
     */
    public SetGen<E> getUnion(SetGen<E> o){
        SetGen<E> newSet = new SetGen<E>();
        for(E element: this.getSet()){
            newSet.add(element);
        }
        for(E element: o.getSet()){
            if(!m_list.contains(element) && !newSet.getSet().contains(element)){
                newSet.add(element);
            }
        }
        return newSet;
    }

    /**
     * Make this set into a difference with a given set.
     * @param o The set to make a difference with.
     */
    public void makeIntersection(SetGen<E> o){
        for(E element: o.getSet()){
            if(m_list.contains(element)){
                this.remove(element);
            }
        }
    }

    /**
     * Make this set into an intersection with a given set.
     * @param o The set with which to make an intersection.
     */
    public void makeDifference(SetGen<E> o){
        for(E element: o.getSet()){
            if(m_list.contains(element)){
                this.remove(element);
            }else if(!m_list.contains(element)){
                this.add(element);
            }
        }
    }

    /**
     * Make a new set with an intersection of this set and a given set.
     * @param o The given set to intersect with.
     * @return The new set that is an intersection of this set and the given set.
     */
    public SetGen<E> getDifference(SetGen<E> o){
        SetGen<E> newSet = new SetGen<E>();
        for(E element: o.getSet()){
            if(m_list.contains(element)){
                newSet.add(element);
            }
        }
        return newSet;
    }

    @Override
    public String toString() {
        return "SetGen{" +
                "m_list=" + m_list +
                '}';
    }
}
