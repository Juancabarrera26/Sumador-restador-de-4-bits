# Sumador–Restador de 4 Bits 

## Descripción general

Esta actividad implementa un sumador–restador de 4 bits simulando el comportamiento de un circuito digital real, utilizando exclusivamente compuertas lógicas AND, OR y NOT.  
El objetivo es replicar la lógica interna del hardware digital, evitando el uso de operadores aritméticos (`+`, `-`) u operadores binarios propios del lenguaje de programación.

La operación realizada se controla mediante un bit de modo `M`:

- `M = 0` → Suma binaria (`A + B`)
- `M = 1` → Resta binaria (`A - B`)

---

## Restricciones cumplidas

El diseño cumple estrictamente con las condiciones del ejercicio académico:

- No se utilizan operadores aritméticos (`+`, `-`)
- No se utilizan operadores bitwise (`&`, `|`, `^`, `~`, `<<`, `>>`)
- La lógica se implementa solo con AND, OR y NOT
- La compuerta XOR se construye a partir de AND, OR y NOT
- Operación exclusiva sobre números binarios de 4 bits
- Entradas y salidas en formato binario

---

## Compuertas lógicas básicas

Se definen las siguientes compuertas lógicas fundamentales:

- AND  
- OR  
- NOT  

Estas funciones simulan directamente el comportamiento de las compuertas físicas y trabajan únicamente con valores binarios (0 y 1).

---

## Implementación de la compuerta XOR

Dado que la compuerta XOR no está permitida directamente, se implementa utilizando la identidad booleana clásica:

\[
A \oplus B = (A \land \lnot B) \lor (\lnot A \land B)
\]

Esta implementación es estándar en lógica digital y permite construir circuitos más complejos usando únicamente compuertas básicas.

---

## Sumador completo (Full Adder)

El sistema se basa en un sumador completo, el cual recibe tres entradas:

- A: bit del primer operando  
- B: bit del segundo operando  
- Cin: acarreo de entrada  

Y produce dos salidas:

- S: bit de suma  
- Cout: acarreo de salida  

Las ecuaciones implementadas son:

\[
S = A \oplus B \oplus Cin
\]

\[
Cout = (A \land B) \lor (Cin \land (A \oplus B))
\]

Este módulo constituye el bloque fundamental del circuito.

---

## Sumador–Restador de 4 bits (Ripple Carry)

El sumador–restador se construye encadenando cuatro sumadores completos, propagando el acarreo desde el bit menos significativo (LSB) hasta el bit más significativo (MSB).  
Este esquema se conoce como Ripple Carry Adder.

---

## Implementación de la resta (Complemento a dos)

La resta binaria se implementa mediante el método de complemento a dos, basado en la identidad:

\[
A - B = A + (\lnot B + 1)
\]

Para lograr esto con un único circuito:

- Cada bit de B se invierte condicionalmente usando `B XOR M`
- El bit M se inyecta como acarreo inicial (`Cin = M`)

De esta forma:

- Si M = 0, el circuito funciona como sumador  
- Si M = 1, el circuito realiza la resta usando complemento a dos  

Este enfoque permite reutilizar el mismo hardware para ambas operaciones.

---

## Entradas y salidas

### Entradas
- A: número binario de 4 bits (ejemplo: `0110`)
- B: número binario de 4 bits (ejemplo: `0010`)
- M: bit de control (0 para suma, 1 para resta)

### Salidas
- Resultado binario de 4 bits
- Cout: acarreo final del circuito

Nota: el valor Cout se entrega como salida del circuito, pero no se analiza overflow, ya que el ejercicio trabaja con aritmética binaria sin signo.

---

## Pruebas realizadas

El programa incluye pruebas automáticas para validar el correcto funcionamiento del circuito:

| Operación | Resultado |
|----------|-----------|
| `0011 + 0101` | `1000` |
| `0111 + 0001` | `1000` |
| `0110 - 0010` | `0100`
