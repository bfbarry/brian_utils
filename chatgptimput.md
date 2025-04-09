Fill in the blanks of the following generic linked list class called GenericLinkedList. It should contain:

- a constructor with the following signature: GenericLinkedList()
- an inner Node class definition
- a method called kindLatin that traverses through the list and prints out the concatenation of each node's toString value and the String "pls".

To illustrate, consider the following linked list of Strings:

`"rome" --> "venice" --> "milan" --> "pisa"`

The program would print out:

```
romepls
venicepls
milanpls
pisapls
```

```java
public class ____1____<____2____> {
    ____3____ class ____4____<E> {
        E data;
        Node<E> next;
        Node(__5__ data, Node<E> ____6____) {
            this.data = data;
            this.next = next;
        }
    }
    private ____7____<____8____> head;
    public GenericLinkedList() {
        head = null;
    }
    public void kindLatin() {
        Node<T> ____9____ = head;
        while (____10____  ____11____ null) {
            System.out.println(current.____12____.toString() + ____13____);
            current = current.next;
        }
    }
}
```

Basically fill in where ____<number>____ is in the code above. Structure your output like this:
1: <code>
2: <code>
etc.
