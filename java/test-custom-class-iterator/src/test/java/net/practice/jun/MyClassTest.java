package net.practice.jun;

import org.junit.Test;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class MyClassTest  {
  @Test
  public void testMyClass() {
    List<String> strs = new ArrayList<String>();
    strs.add("str0-0");
    strs.add("str0-1");
    MyClass mc0 = new MyClass(0, strs);
    Iterator<String> mc0It = mc0.iterator();
    while ( mc0It.hasNext() )
      System.out.println(mc0It.next());

    strs = new ArrayList<String>();
    strs.add("str10-0");
    strs.add("str10-1");
    strs.add("str10-2");
    strs.add("str10-3");
    MyClass mc1 = new MyClass(10, strs);

    strs = new ArrayList<String>();
    strs.add("str20-0");
    strs.add("str20-1");
    strs.add("str20-2");
    MyClass mc2 = new MyClass(20, strs);

    assertEquals(0, mc0.i);
    assertEquals(2, mc0.strs.size());
    assertEquals(10, mc1.i);
    assertEquals(4, mc1.strs.size());
    assertEquals(20, mc2.i);
    assertEquals(3, mc2.strs.size());

    List<MyClass> myClassList = new ArrayList<MyClass>();
    myClassList.add(mc0);
    myClassList.add(mc1);
    myClassList.add(mc2);
    //MyClassList<MyClass> myClasses = new MyClassList<MyClass>(new MyClass[]{mc0, mc1, mc2});
    //MyClassList<MyClass> myClasses = new MyClassList<MyClass>(myClassList);
    Iterator<MyClass> it = myClassList.iterator();
    while ( it.hasNext() )  {
      MyClass mc = it.next();
      Iterator<String> mcIt = mc.iterator();
      System.out.println(mc.i);
      while ( mcIt.hasNext() )
        System.out.println("\t" + mcIt.next());
    }
  }
}
