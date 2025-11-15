#include <iostream>
#include <iomanip>
#include "mat.h"

//Функция для вычисления детерминанта (рекурсивно)
template<typename T>
T determinant(const Matrix<T>& mat) {
    unsigned n = mat.rows();
    
    if (n == 1) return mat(0, 0);
    if (n == 2) return mat(0, 0) * mat(1, 1) - mat(0, 1) * mat(1, 0);
    
    T det = 0;
    for (unsigned j = 0; j < n; j++) {
        Matrix<T> minor(n - 1, n - 1);
        unsigned minor_row = 0;
        
        for (unsigned i = 1; i < n; i++) {
            unsigned minor_col = 0;
            for (unsigned k = 0; k < n; k++) {
                if (k != j) {
                    minor(minor_row, minor_col) = mat(i, k);
                    minor_col++;
                }
            }
            minor_row++;
        }
        
        T sign = (j % 2 == 0) ? 1 : -1;
        det += sign * mat(0, j) * determinant(minor);
    }
    return det;
}

int main() {
    std::cout << std::fixed;
    std::cout.precision(2);
    
    //5x5(25)
    std::cout << "=== Test 1: 5x5 matrix ===" << std::endl;
    Matrix<double> m5 = Matrix<double>::getSpecificDeterminant(5, 10.0);
    double det5 = determinant(m5);
    Matrix<double> m5t = m5.transposed();
    double det5t = determinant(m5t);
    std::cout << "det(M) = " << det5 << std::endl;
    std::cout << "det(M^T) = " << det5t << std::endl;
    std::cout << "Equal: " << (std::abs(det5 - det5t) < 0.01) << std::endl;
    
    //50x50(25 00)
    std::cout << "\n=== Test 2: 50x50 matrix ===" << std::endl;
    Matrix<double> m50 = Matrix<double>::getSpecificDeterminant(50, 5.0);
    std::cout << "Calculating determinant..." << std::endl;
    double det50 = determinant(m50);
    Matrix<double> m50t = m50.transposed();
    double det50t = determinant(m50t);
    std::cout << "det(M) ≈ " << det50 << std::endl;
    std::cout << "det(M^T) ≈ " << det50t << std::endl;
    
    //100x100(1 00 00)
    std::cout << "\n=== Test 3: 100x100 matrix ===" << std::endl;
    Matrix<double> m100 = Matrix<double>::getSpecificDeterminant(100, 2.0);
    std::cout << "This may take a while..." << std::endl;
    double det100 = determinant(m100);
    Matrix<double> m100t = m100.transposed();
    double det100t = determinant(m100t);
    std::cout << "det(M) ≈ " << det100 << std::endl;
    std::cout << "det(M^T) ≈ " << det100t << std::endl;
    
    return 0;
}