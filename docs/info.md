# Multiplicador Secuencial de 4 Bits

## Resumen del Proyecto
Proyecto desarrollado por Esteban UNAL

Este diseño implementa un **circuito multiplicador de 4 bits con arquitectura secuencial** basado en el algoritmo de suma y desplazamiento. El sistema procesa dos números binarios de 4 bits sin signo (denominados A y B) y produce un producto final de 8 bits (PP). La característica principal es su operación paso a paso, donde cada bit se procesa en un ciclo de reloj individual, optimizando así el uso de recursos en implementaciones ASIC.

## Metodología de Operación

El circuito implementa el **algoritmo de suma y desplazamiento**:

1. **Preparación Inicial**: Cuando se activa la entrada `init`, el sistema carga los valores A y B en sus respectivos registros internos y limpia el acumulador.

2. **Procesamiento Iterativo**: En cada pulso de reloj:
   - Se verifica el bit de menor peso de B
   - Cuando este bit vale 1, el valor de A se agrega al acumulador
   - Ambos valores se recorren una posición a la derecha
   - Este ciclo se repite mientras B sea diferente de cero

3. **Término de Operación**: La bandera `done` señaliza que el cálculo ha terminado y el producto está listo para lectura.

## Componentes del Sistema

La arquitectura está compuesta por cinco bloques funcionales:

- **RSR (Registro de Recorrido Derecho)**: Procesa el operando B bit por bit mediante desplazamientos a la derecha
- **LSR (Registro de Recorrido Izquierdo)**: Ajusta el operando A mediante desplazamientos a la izquierda para mantener el alineamiento correcto
- **ACC (Acumulador)**: Suma progresivamente los productos intermedios hasta obtener el resultado completo
- **COMP (Comparador)**: Verifica cuándo B llega a cero, señalando el fin del proceso
- **Unidad de Control**: FSM encargada de gestionar toda la secuencia operativa

## Características Temporales

El tiempo de multiplicación varía entre **4 y 5 ciclos de reloj** según los operandos:
- Caso óptimo: 4 ciclos (B contiene ceros en posiciones menos significativas)
- Caso pesimista: 5 ciclos (configuración más lenta)

## Descripción de Conexiones

### Entradas (ui)
- `ui[3:0]`: Operando A (primer valor de 4 bits)
- `ui[7:4]`: Operando B (segundo valor de 4 bits)

### Salidas (uo)
- `uo[7:0]`: PP - Producto resultante (8 bits)

### Bidireccionales (uio)
- `uio[0]`: init - Señal de arranque (entrada)
- `uio[1]`: done - Indicador de operación terminada (salida)

## Procedimiento de Uso

1. Configurar los valores A y B en las entradas correspondientes
2. Generar un pulso positivo en la señal `init` para comenzar
3. Monitorear la señal `done` hasta que cambie a estado alto
4. Capturar el producto de 8 bits disponible en `PP`
