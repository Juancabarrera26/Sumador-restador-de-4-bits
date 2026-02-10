# Compuertas Lógicas Básicas 
def gate_and(a, b): return 1 if a == 1 and b == 1 else 0
def gate_or(a, b):  return 1 if a == 1 or b == 1 else 0
def gate_not(a):    return 1 if a == 0 else 0

def gate_xor(a, b):
    # Implementación académica: (a · b') + (a' · b)
    return gate_or(gate_and(a, gate_not(b)), gate_and(gate_not(a), b))

#  Módulos de Hardware 
def full_adder(a, b, cin):
    # S = A ⊕ B ⊕ Cin
    axorb = gate_xor(a, b)
    s = gate_xor(axorb, cin)
    # Cout = (A · B) + (Cin · (A ⊕ B))
    cout = gate_or(gate_and(a, b), gate_and(cin, axorb))
    return s, cout

# Implementación de un sumador-restador de 4 bits tipo ripple-carry.
# La resta se procesa en complemento a dos (A - B = A + B' + 1) mediante 
# la inversión bit a bit (B XOR M) y la inyección del bit M como carry inicial.
def adder_subtractor_4bit(A_str, B_str, M_str):
    A = [int(bit) for bit in A_str]
    B = [int(bit) for bit in B_str]
    M = int(M_str)
    
    res = [0] * 4
    carry = M  # M=0 para suma, M=1 para resta (carry inicial para C2)

    # Propagación del carry de LSB a MSB (Ripple Carry)
    for i in range(3, -1, -1):
        b_mod = gate_xor(B[i], M)
        res[i], carry = full_adder(A[i], b_mod, carry)
        
    return "".join(map(str, res)), str(carry)

# Pruebas de Validación Binaria 
def run_tests():
    # Estructura: (A, B, M, Resultado Esperado, Cout Esperado)
    tests = [
        ("0011", "0101", "0", "1000", "0"),
        ("0111", "0001", "0", "1000", "0"),
        ("0110", "0010", "1", "0100", "1"),
        ("0101", "0101", "1", "0000", "1")
    ]
    
    print(f"{'Operación':<12} | {'M':<2} | {'Resultado':<6} | {'Cout':<4} | {'Status'}")
    print("-" * 45)
    for a, b, m, exp_res, exp_cout in tests:
        res, cout = adder_subtractor_4bit(a, b, m)
        op = "+" if m == "0" else "-"
        status = "OK" if (res == exp_res and cout == exp_cout) else "FAIL"
        print(f"{a} {op} {b} | {m} | {res:<6} | {cout:<4} | {status}")

if __name__ == "__main__":
    run_tests()
    
    print("\n--- Entrada Manual ---")
    try:
        a_in = input("A (4 bits): ")
        b_in = input("B (4 bits): ")
        m_in = input("M (0=Suma, 1=Resta): ")
        bin_res, final_cout = adder_subtractor_4bit(a_in, b_in, m_in)
        print(f"\nResultado Binario: {bin_res}")
        print(f"Carry Out Final:   {final_cout}")
    except:
        print("Error: Ingrese solo valores binarios de 4 bits.")

