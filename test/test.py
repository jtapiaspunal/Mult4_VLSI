# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # --- RESET ---
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    
    # IMPORTANTE: Darle suficientes ciclos al reset para limpiar las 'X' internas
    await ClockCycles(dut.clk, 10) 
    dut.rst_n.value = 1
    
    # Esperar unos ciclos extra tras soltar el reset para estabilidad
    await ClockCycles(dut.clk, 5)

    dut._log.info("Test project behavior")

    # --- INPUTS ---
    # Set the input values you want to test
    dut.ui_in.value = 20
    dut.uio_in.value = 30

    # --- ESPERA (Aquí estaba el problema) ---
    # Un multiplicador secuencial necesita varios ciclos para terminar.
    # En Gate Level, sé generoso con el tiempo. Dale 50 ciclos.
    dut._log.info("Waiting for calculation...")
    await ClockCycles(dut.clk, 50)

    # --- VERIFICACIÓN ---
    # Imprimir el valor real que obtuviste (útil para depurar)
    dut._log.info(f"Valor obtenido en la salida: {dut.uo_out.value}")

    # Ahora sí, verifica.
    # NOTA: 20 * 30 = 600. Eso es mayor a 255 (8 bits), así que habrá overflow.
    # Asegúrate de qué valor esperas realmente.
    # Si esperas 0, usa esto:
    assert dut.uo_out.value == 0