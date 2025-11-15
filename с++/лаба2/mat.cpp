#include "subbvectorr"
#include <cmath>
#include <random>

template<typename T>
class Matrix {
    subvector<T> data;
    unsigned cols, rows;

public:
    Matrix(unsigned rows, unsigned cols, T value = 0);

    static Matrix Identity(unsigned n);
    static Matrix getSpecificDeterminant(unsigned n, T determinant);

    unsigned rows() const;
    unsigned cols() const;

    Matrix& transpose();
    Matrix transposed() const;

    T& operator()(unsigned row, unsigned col);
    T operator()(unsigned row, unsigned col) const;
};

template<typename T>
Matrix<T>::Matrix(unsigned rows, unsigned cols, T value) : rows(rows), cols(cols) {
    for (unsigned i = 0; i < rows * cols; i++) {
        data.push_back(value);
    }
}

template<typename T>
Matrix<T> Matrix<T>::Identity(unsigned n) {
    Matrix<T> result(n, n, 0);
    for (unsigned i = 0; i < n; i++) {
        result(i, i) = 1;
    }
    return result;
}

template<typename T>
Matrix<T> Matrix<T>::getSpecificDeterminant(unsigned n, T determinant) {
    Matrix<T> result = Identity(n);
    result(0, 0) = determinant;  //диагональная матрица
    return result;
}

template<typename T>
unsigned Matrix<T>::rows() const {
    return rows;
}

template<typename T>
unsigned Matrix<T>::cols() const {
    return cols;
}

template<typename T>
Matrix<T>& Matrix<T>::transpose() {
    Matrix<T> temp(cols, rows);
    for (unsigned i = 0; i < rows; i++) {
        for (unsigned j = 0; j < cols; j++) {
            temp(j, i) = (*this)(i, j);
        }
    }
    *this = temp;
    return *this;
}

template<typename T>
Matrix<T> Matrix<T>::transposed() const {
    Matrix<T> result(cols, rows);
    for (unsigned i = 0; i < rows; i++) {
        for (unsigned j = 0; j < cols; j++) {
            result(j, i) = (*this)(i, j);
        }
    }
    return result;
}

template<typename T>
T& Matrix<T>::operator()(unsigned row, unsigned col) {
    return data[row * cols + col];
}

template<typename T>
T Matrix<T>::operator()(unsigned row, unsigned col) const {
    return data[row * cols + col];
}