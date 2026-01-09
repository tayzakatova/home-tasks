template<typename T>
class subforwardlist {
    struct Node {
        T data;
        Node* next;
    };

    Node* begin;

public:

    subforwardlist();
    ~subforwardlist();
    subforwardlist(const subforwardlist& other);
    subforwardlist& operator=(const subforwardlist& other);
    subforwardlist(subforwardlist&& other);
    subforwardlist& operator=(subforwardlist&& other);

    void push_back(const T& data);
    T pop_back();
    void push_forward(const T& data);
    T pop_forward();
    void push_where(unsigned int where, const T& data);
    T erase_where(unsigned int where);
    unsigned int size();
};

template<typename T>
subforwardlist<T>::subforwardlist() : begin(nullptr) {}

template<typename T>
subforwardlist<T>::~subforwardlist() {
    while (begin) {
        Node* temp = begin;
        begin = begin->next;
        delete temp;
    }
}

template<typename T>
subforwardlist<T>::subforwardlist(const subforwardlist& other) : begin(nullptr) {
    if (!other.begin) return;
    
    Node* other_current = other.begin;
    begin = new Node{other_current->data, nullptr};
    Node* current = begin;
    other_current = other_current->next;
    
    while (other_current) {
        current->next = new Node{other_current->data, nullptr};
        current = current->next;
        other_current = other_current->next;
    }
}

template<typename T>
subforwardlist<T>& subforwardlist<T>::operator=(const subforwardlist& other) {   // Тут абсолютно аналогичные замечание про copy&swap
    if (this == &other) return *this;
    
    while (begin) {
        Node* temp = begin;
        begin = begin->next;
        delete temp;
    }
    begin = nullptr;
    
    if (!other.begin) return *this;
    
    Node* other_current = other.begin;
    begin = new Node{other_current->data, nullptr};
    Node* current = begin;
    other_current = other_current->next;
    
    while (other_current) {
        current->next = new Node{other_current->data, nullptr};
        current = current->next;
        other_current = other_current->next;
    }
    return *this;
}

template<typename T>
subforwardlist<T>::subforwardlist(subforwardlist&& other) : begin(other.begin) {
    other.begin = nullptr;
}

template<typename T>
subforwardlist<T>& subforwardlist<T>::operator=(subforwardlist&& other) {  // замечание аналогично муву в векторе
    if (this == &other) return *this;
    
    while (begin) { // этот кусок кода можно было вынести в отдельные метод, так как он часто встречается
        Node* temp = begin;
        begin = begin->next;
        delete temp;
    }
    
    begin = other.begin;
    other.begin = nullptr;
    return *this;
}

// Здесь и далее неявно используется код, который ищет указатель на ноду по индексу, это можно было вынести в отдельный метод и переиспользовать везд

template<typename T>
void subforwardlist<T>::push_back(const T& data) {
    if (!begin) {
        begin = new Node{data, nullptr};
        return;
    }
    
    Node* current = begin;
    while (current->next) {
        current = current->next;
    }
    current->next = new Node{data, nullptr};
}

template<typename T>
T subforwardlist<T>::pop_back() {
    if (!begin) return T{};
    
    if (!begin->next) {
        T value = begin->data;
        delete begin;
        begin = nullptr;
        return value;
    }
    
    Node* current = begin;
    while (current->next->next) {
        current = current->next;
    }
    
    T value = current->next->data;
    delete current->next;
    current->next = nullptr;
    return value;
}

template<typename T>
void subforwardlist<T>::push_forward(const T& data) {
    Node* new_node = new Node{data, begin};
    begin = new_node;
}

template<typename T>
T subforwardlist<T>::pop_forward() {
    if (!begin) return T{};
    
    Node* temp = begin;
    T value = begin->data;
    begin = begin->next;
    delete temp;
    return value;
}

template<typename T>
void subforwardlist<T>::push_where(unsigned int where, const T& data) {
    if (where == 0) {
        push_forward(data);
        return;
    }
    
    Node* current = begin;
    for (unsigned int i = 0; i < where - 1 && current; i++) {
        current = current->next;
    }
    
    if (!current) return;
    
    Node* new_node = new Node{data, current->next};
    current->next = new_node;
}

template<typename T>
T subforwardlist<T>::erase_where(unsigned int where) {
    if (!begin) return T{};
    
    if (where == 0) {
        return pop_forward();
    }
    
    Node* current = begin;
    for (unsigned int i = 0; i < where - 1 && current->next; i++) {
        current = current->next;
    }
    
    if (!current || !current->next) return T{};
    
    Node* to_delete = current->next;
    T value = to_delete->data;
    current->next = to_delete->next;
    delete to_delete;
    return value;
}
// По-хорошему size нужно хранить полем, а не считать за O(N) 
template<typename T>
unsigned int subforwardlist<T>::size() {
    unsigned int count = 0;
    Node* current = begin;
    while (current) {
        count++;
        current = current->next;
    }
    return count;

}
