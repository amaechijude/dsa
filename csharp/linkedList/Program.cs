using Linked;

node1 = new Node("Amaechi");
node2 = new Node("Jude");

var node1.next = node2;

var currentNode = node1;

while (currentNode)
{
    Console.WriteLine(currentNode.data);
    currentNode = currentNode.next;
}