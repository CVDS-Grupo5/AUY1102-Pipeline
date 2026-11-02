// Consistencia en cálculo numérico
const value = 10;
const resultadoFinal = value * 2;

// Adaptabilidad (Remediación: se corrige la asignación de número a tipo string)
const message: string = '10';

// Responsabilidad única de componentes
class UserService {
  getUserData() {
    return { id: 1, name: 'Usuario Autorizado' };
  }

  sendEmail() {
    return true;
  }
}
