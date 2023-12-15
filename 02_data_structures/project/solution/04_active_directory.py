




class QueueNode:
    
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, value):
        new_node = QueueNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
            
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value          # copy the value to a local variable
        self.head = self.head.next       # shift the head (i.e., the front of the queue)
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
        
    def to_list(self):
        elements = []
        
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
            
        return elements

    # def __repr__(self):
    #     if len(self.q) > 0:
    #         s = "<enqueue here>\n_________________\n" 
    #         s += "\n_________________\n".join([str(item) for item in self.q])
    #         s += "\n_________________\n<dequeue here>"
    #         return s
    #     else:
    #         return "<queue is empty>"






class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    
    def __str__(self):
        return f"Group({self.name})"

    def __repr__(self):
        return f"Group({self.name})"


def print_groups_tree(group: Group, level=0):
    # print(group.name)
    level += 1
    out_group = "\t"*level + f" {group.name} -> "
    for user in group.users:
        out_group += f"{user} "
    out_group += "\n"
    for child_group in group.get_groups():
        out_group += print_groups_tree(child_group, level)

    return out_group



def is_user_in_group(user_id, main_group: Group):

    queue = Queue()
    visit_order = []

    node = main_group

    queue.enqueue(node)
    while(queue.size() > 0):
        node: Group = queue.dequeue()
        visit_order.append(node)

        users = node.get_users()
        for user in users:
            if user == user_id:
                return visit_order

        groups = node.get_groups()
        if len(groups) > 0:
            for group in groups:
                queue.enqueue(group)

    return visit_order


def create_users(group: Group, users):
    users_sample = users[:2]
    users = users[2:]
    for user in users_sample:
        group.add_user(user)

    return users


if __name__ == "__main__":

    n_users = 10
    users = [f"{i}" for i in range(n_users)]
    search_user = users[-1]

    n_levels = 2

    # Create random active directory
    level = 1
    main_group = Group(f"Name: {level}")
    users = create_users(main_group, users)

    level += 1
    while len(users) > 0:
        child_group = Group(f"Name: {level}")
        users = create_users(child_group, users)
        main_group.add_group(child_group)

    # Search user
    visit_order = is_user_in_group(search_user, main_group)
    print(search_user in visit_order[-1].users)

    print()
    print("*"*60)
    print("Tree")
    groups_tree = print_groups_tree(main_group, level=0)

    print(groups_tree)
    print()
    print("*"*60)