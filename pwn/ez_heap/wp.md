
- fastbin是单链表后进先出结构，使用chunk中的fd指针连接。

- 当两次free后，b和c进入fastbin，里面的顺序为b->c->NULL

- a，b，c物理上是相邻的

- a覆盖payload后，b的size字段被修改为0x21(没变，逃避glibc检查)；fd最低字节变为0x60(指向target)

- 再次分配，e为之前分配的c；由于这时b的fd已经修改，所以再次分配就变成了target，即e=target

可以使用pwndbg插件配合gdb调试exp.py，便于理解覆盖过程。