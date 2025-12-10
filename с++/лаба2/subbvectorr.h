template<typename T>
class subvector {
    T *mas;
    unsigned int top;
    unsigned int capacity;
     
public:
    //Конструкторы(лего) и правило пяти
    subvector();
    ~subvector();
    subvector(const subvector& other);
    subvector& operator=(const subvector& other);
    subvector(subvector&& other);
    subvector& operator=(subvector&& other);

    //бэйзик методы
    bool push_back(const T& d);
    T pop_back();
    bool resize(unsigned int new_capacity);
    void shrink_to_fit();
    void clear();
    T& operator[](unsigned int index);
    const T& operator[](unsigned int index) const;
    unsigned int size() const;
    unsigned int get_capacity() const;
};
// Нет ну так по красоте конечно
template<typename T>
subvector<T>::subvector() : mas(nullptr), top(0), capacity(0) {}

template<typename T>
subvector<T>::~subvector() {
    delete[] mas;
}

template<typename T>
subvector<T>::subvector(const subvector& other) : mas(nullptr), top(0), capacity(0) {
    if (other.capacity > 0) {
        mas = new T[other.capacity];
        for (unsigned int i = 0; i < other.top; i++) {
            mas[i] = other.mas[i];
        }
        top = other.top;
        capacity = other.capacity;  // это тоже загоняется в список инициализации
    }
}

template<typename T>
subvector<T>& subvector<T>::operator=(const subvector& other) {
    if (this != &other) {
        delete[] mas;
        // код ниже похож на логику копирующего конструктора. с помощью copy&swap можно было переиспользовать имеющийся код
        if (other.capacity > 0) {
            mas = new T[other.capacity];
            for (unsigned int i = 0; i < other.top; i++) {
                mas[i] = other.mas[i];
            }
            top = other.top;
            capacity = other.capacity;
        } else {
            mas = nullptr;
            top = 0;
            capacity = 0;
        }
    }
    return *this;
}

template<typename T>
subvector<T>::subvector(subvector&& other) : mas(other.mas), top(other.top), capacity(other.capacity) {
    other.mas = nullptr;
    other.top = 0;
    other.capacity = 0;
}

template<typename T>
subvector<T>& subvector<T>::operator=(subvector&& other) {
    if (this != &other) {
        delete[] mas;
        
        mas = other.mas;
        top = other.top;
        capacity = other.capacity;
        
        other.mas = nullptr;
        other.top = 0;
        other.capacity = 0;
    }
    return *this;
    // Тут правильнее не удалять себя (это долго), а отдать свое состояние внутрь other, так как это move операция, то такое поведение корректно
}

template<typename T>
bool subvector<T>::push_back(const T& d) {
    if (top >= capacity) {
        unsigned int new_capacity = (capacity == 0) ? 1 : capacity * 2;
        if (!resize(new_capacity)) return false;
    }
    mas[top] = d;
    top++;
    return true;
}

template<typename T>
T subvector<T>::pop_back() {
    if (top == 0) return T{};
    top--;
    return mas[top];
}

template<typename T>
bool subvector<T>::resize(unsigned int new_capacity) {
    if (new_capacity < top) {
        top = new_capacity;
    }
    
    T* new_mas = new T[new_capacity];
    if (new_mas == nullptr) return false;
    
    for (unsigned int i = 0; i < top; i++) {
        new_mas[i] = mas[i];
    }
    
    delete[] mas;
    mas = new_mas;
    capacity = new_capacity;
    return true;
}

template<typename T>
void subvector<T>::shrink_to_fit() {
    if (top < capacity) {
        resize(top);
    }
}

template<typename T>
void subvector<T>::clear() {
    top = 0;
}

template<typename T>
T& subvector<T>::operator[](unsigned int index) {
    return mas[index];
}

template<typename T>
const T& subvector<T>::operator[](unsigned int index) const {
    return mas[index];
}

template<typename T>
unsigned int subvector<T>::size() const {
    return top;
}

template<typename T>
unsigned int subvector<T>::get_capacity() const {
    return capacity;

}
