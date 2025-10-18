def tarifa(t_auto,t_moto,t_bici,mensualidad):
    while True:
        print("\n" + "="*50)
        print("║" + " "*15 + "MENÚ TARIFAS" + " "*23 + "║")
        print("="*50)
        print("║  1. Ingresar tarifas" + " "*29 + "║")
        print("║  2. Mostrar tarifas" + " "*30 + "║")
        print("║  3. Modificar tarifas" + " "*28 + "║")
        print("║  4. Regresar al menú principal" + " "*19 + "║")
        print("="*50)
        
        opc = input("➤ Digite una opción: ")
        
        if opc == "1":
            t_auto,t_moto,t_bici,mensualidad = ingresar_tarifa(t_auto,t_moto,t_bici,mensualidad)
        elif opc == "2":
            mostrar_tarifas(t_auto,t_moto,t_bici,mensualidad)
        elif opc == "3":
            t_auto,t_moto,t_bici,mensualidad = modificar_tarifas(t_auto,t_moto,t_bici,mensualidad)
        elif opc == "4":
            return t_auto,t_moto,t_bici,mensualidad
        else:
            print("\n❌ Opción inválida. Por favor intente nuevamente.")

def ingresar_tarifa (t_auto,t_moto,t_bici,mensualidad):
     while True:
        print("\n" + "="*50)
        print("║" + " "*12 + "INGRESAR TARIFAS" + " "*22 + "║")
        print("="*50)
        print("║  1. Ingresar Tarifa de Automóvil" + " "*17 + "║")
        print("║  2. Ingresar Tarifa de Motocicleta" + " "*15 + "║")
        print("║  3. Ingresar Tarifa de Bicicleta" + " "*17 + "║")
        print("║  4. Ingresar Tarifa de Mensualidad para Autos" + " "*3 + "║")
        print("║  5. Regresar al sub Menú Tarifas" + " "*17 + "║")
        print("="*50)
                
        opc = input("➤ Digite una opción: ")
        if opc == "1":
            while True:
                try:
                    t_auto = int(input("💵 Ingresa el valor a cobrar por minuto para automóviles: "))
                    break                
                except ValueError:
                    print("❌ Valor inválido. Debe ingresar un número.")
        elif opc == "2":
            while True:
                try:
                    t_moto = int(input("💵 Ingresa el valor a cobrar por minuto para motocicletas: "))
                    break
                except ValueError:
                    print("❌ Valor inválido. Debe ingresar un número.")
        elif opc == "3":
            while True:
                try:
                    t_bici = int(input("💵 Ingresa el valor a cobrar por minuto para bicicletas: "))
                    break
                except ValueError:
                    print("❌ Valor inválido. Debe ingresar un número.")

        elif opc == "4":
            while True:
                    try:
                        mensualidad = int(input("💵 Ingresa el valor de la mensualidad: "))
                        break
                    except ValueError:
                        print("❌ Valor inválido. Debe ingresar un número.")
        
        elif opc == "5":
            return t_auto,t_moto,t_bici,mensualidad         
        else:
            print("\n❌ Opción inválida. Por favor intente nuevamente.")

def mostrar_tarifas(t_auto,t_moto,t_bici,mensualidad):
    print("\n" + "="*50)
    print("║" + " "*17 + "TARIFAS" + " "*26 + "║")
    print("="*50)
    print(f"║  🚗 Valor por minuto Auto:        ${t_auto:<15}║")
    print(f"║  🏍️  Valor por minuto Moto:        ${t_moto:<15}║")
    print(f"║  🚲 Valor por minuto Bicicleta:   ${t_bici:<15}║")
    print(f"║  📅 Mensualidad para Autos:       ${mensualidad:<15}║")
    print("="*50)
    input("\n⏎ Presiona Enter para continuar...")

def modificar_tarifas(t_auto,t_moto,t_bici,mensualidad):
    while True:
        print("\n" + "="*50)
        print("║" + " "*12 + "MODIFICAR TARIFAS" + " "*21 + "║")
        print("="*50)
        print("║  1. Modificar Tarifa Automóvil" + " "*19 + "║")
        print("║  2. Modificar Tarifa Motocicleta" + " "*17 + "║")
        print("║  3. Modificar Tarifa Bicicleta" + " "*19 + "║")
        print("║  4. Modificar Tarifa Mensualidad para Autos" + " "*5 + "║")
        print("║  5. Regresar al sub Menú Tarifas" + " "*17 + "║")
        print("="*50)
                
        opc = input("➤ Digite una opción: ")
        if opc == "1":
            while True:
                try:
                    t_auto = int(input("💵 Ingresa el valor a cobrar por minuto para automóviles: "))
                    break                
                except ValueError:
                    print("❌ Valor inválido. Debe ingresar un número.")
        elif opc == "2":
            while True:
                try:
                    t_moto = int(input("💵 Ingresa el valor a cobrar por minuto para motocicletas: "))
                    break
                except ValueError:
                    print("❌ Valor inválido. Debe ingresar un número.")
        elif opc == "3":
            while True:
                try:
                    t_bici = int(input("💵 Ingresa el valor a cobrar por minuto para bicicletas: "))
                    break
                except ValueError:
                    print("❌ Valor inválido. Debe ingresar un número.")

        elif opc == "4":
            while True:
                    try:
                        mensualidad = int(input("💵 Ingresa el valor de la mensualidad: "))
                        break
                    except ValueError:
                        print("❌ Valor inválido. Debe ingresar un número.")
        
        elif opc == "5":
            return t_auto,t_moto,t_bici,mensualidad         
        else:
            print("\n❌ Opción inválida. Por favor intente nuevamente.")


def registrar_mensualidad (mensualidad,numero_factura,lmensualidad,mensualidadl):
    while True:
            try:

                numero_p = input("🚗 Ingrese el número de la placa (auto: 3 letras + 3 números): ").upper()
                if len(numero_p) != 6 or not numero_p[:3].isalpha() or not numero_p[3:].isdigit():
                    print("❌ Formato de placa inválido para automóvil (debe ser 3 letras + 3 números)")
                    continue
                if numero_p in lmensualidad:
                        print("❌ Placa ya registrada")
                        continue
                fecha_i = int(input("📅 Digite la fecha de ingreso (ddmmyyyy): "))
                
                diai = fecha_i // 1000000
                mesi = (fecha_i % 1000000) // 10000
                añoi = fecha_i % 10000
                
                if diai < 1 or diai > 31:
                    print("❌ Día inválido (debe estar entre 01-31)")
                    continue
                if mesi < 1 or mesi > 12:
                    print("❌ Mes inválido (debe estar entre 01-12)")
                    continue
                if añoi < 2000 or añoi > 2100:
                    print("❌ Año inválido")
                    continue
                
                break
            except ValueError:
                print("❌ Debe ingresar un número válido para la fecha")
    diaf = diai + 29
    mesf = mesi
    añof = añoi
    if diaf > 31:
        mesf +=1
        diaf -= 31
        if mesi == 12:
            añof += 1
            mesf = 1
    
    fecha_ingreso = diai,mesi,añoi
    fecha_final = diaf,mesf,añof
    cliente = input("👤 Digite su nombre: ").strip()
    total = mensualidad
    

    print("\n" + "="*50)
    print("║" + " "*12 + "FACTURA MENSUALIDAD" + " "*19 + "║")
    print("="*50)
    print(f"║  Factura No:              {numero_factura:<22}║")
    print(f"║  🚗 Num Placa del auto:    {numero_p:<22}║")
    print(f"║  📅 Fecha ingreso:         {diai:02d}/{mesi:02d}/{añoi:<18}║")
    print(f"║  📅 Vigencia hasta:        {diaf:02d}/{mesf:02d}/{añof:<18}║")
    print(f"║  👤 Nombre:                {cliente:<22}║")
    print(f"║  💰 Total:                 ${total:<21}║")
    print("="*50)

    men = {
        'Factura No': numero_factura,
        'Num Placa del auto': numero_p,
        'Fecha ingreso': fecha_ingreso,
        'Vigencia hasta': fecha_final,
        'Nombre': cliente,
        'Total': total,
    }
    numero_factura += 1
    lmensualidad.append(numero_p)
    mensualidadl.append(men)
    return numero_factura, lmensualidad, mensualidadl

def ingresar_vehiculo(lregistro,fac_registro,lplacas,consecutivo,lmensualidad):
    minutos = ""
    totali = ""
    horas = ""
    rmensualidad = ""
    salida = "sin salida"
    while True:
        tipo = input("🚗 Tipo de vehículo (a: automóvil, m: moto, b: bicicleta): ").lower()     

        if tipo != "a" and tipo != "b" and tipo != "m":
            print("❌ Tipo de vehículo inválido")
            continue
        i_placa = ""
        
        if tipo == "a" or tipo == "m":
            i_placa = input("🔢 Digite su número de placa (auto: 3 letras + 3 números, moto: 3 letras + 2 números + 1 letra): ").upper()
            
            if tipo == "a":
                if len(i_placa) != 6 or not i_placa[:3].isalpha() or not i_placa[3:].isdigit():
                    print("❌ Formato de placa inválido para automóvil (debe ser 3 letras + 3 números)")
                    continue
            elif tipo == "m":
                if len(i_placa) != 6 or not i_placa[:3].isalpha() or not i_placa[3:5].isdigit() or not i_placa[5].isalpha():
                    print("❌ Formato de placa inválido para moto (debe ser 3 letras + 2 números + 1 letra)")
                    continue
            if i_placa in lplacas:
                print("❌ Placa ya registrada")
                continue
            if i_placa in lmensualidad:
                rmensualidad = "vigente"
            else:
                rmensualidad = "no vigente"

        while True:
            try:
                hora_i = int(input("🕐 Digite la hora (formato 24 horas: hhmm): "))
                h = hora_i // 100
                m = hora_i % 100

                if h < 0 or h > 23 or m < 0 or m > 59:
                    print("❌ Hora inválida (hora debe estar entre 00-23 y minutos entre 00-59)")
                    continue
                break
            except ValueError:
                print("❌ Debe ingresar un número válido")

        while True:
            try:
                fecha_in = int(input("📅 Digite la fecha de ingreso (ddmmyyyy): "))
                
                dia = fecha_in // 1000000
                mes = (fecha_in % 1000000) // 10000
                año = fecha_in % 10000
                
                if dia < 1 or dia > 31:
                    print("❌ Día inválido (debe estar entre 01-31)")
                    continue
                if mes < 1 or mes > 12:
                    print("❌ Mes inválido (debe estar entre 01-12)")
                    continue
                if año < 2000 or año > 2100:
                    print("❌ Año inválido")
                    continue
                
                break
            except ValueError:
                print("❌ Debe ingresar un número válido para la fecha")

        nombre = input("👤 Digite su nombre: ").strip()
        
        if nombre == "":
            print("❌ El nombre no puede estar vacío")
            continue

        fac_registro += 1

        if tipo == "a":
            registro = {
                'Factura No': fac_registro,
                'Num Placa': i_placa,
                'Vehiculo tipo': "Auto",
                'Fecha de ingreso': fecha_in,
                'Mensualidad': rmensualidad,
                'Hora de ingreso': hora_i,
                'Hora de salida': horas,
                'Nombre': nombre,
                'Numero minutos': minutos,
                'Total': totali,
                'h': h,
                'm': m,
                's': salida
            }
            lplacas.append(i_placa)
        
        elif tipo == "m":
            registro = {
                'Factura No': fac_registro,
                'Num Placa': i_placa, 
                'Vehiculo tipo': "Moto",
                'Fecha de ingreso': fecha_in,
                'Hora de ingreso': hora_i,
                'Hora de salida': horas,
                'Nombre': nombre,
                'Numero minutos': minutos,
                'Total': totali,
                'h': h,
                'm': m,
                's': salida
            }
            lplacas.append(i_placa)

        elif tipo == "b":
            consecutivo += 1
            registro = {
                'Factura No': fac_registro,
                'Consecutivo': consecutivo, 
                'Vehiculo tipo': "Bicicleta",
                'Fecha de ingreso': fecha_in,
                'Hora de ingreso': hora_i,
                'Hora de salida': horas,
                'Nombre': nombre,
                'Numero minutos': minutos,
                'Total': totali,
                'h': h,
                'm': m,
                's': salida
            }
        
        lregistro.append(registro)
        print("\n" + "="*50)
        print("║" + " "*10 + "✅ VEHÍCULO REGISTRADO EXITOSAMENTE" + " "*5 + "║")
        print("="*50)

        return lplacas, fac_registro, consecutivo, lregistro

def buscar_vehiculo(lregistro):
    while True:
        print("\n" + "="*50)
        print("║" + " "*15 + "BUSCAR VEHÍCULO" + " "*20 + "║")
        print("="*50)
        print("║  1. Buscar motos" + " "*33 + "║")
        print("║  2. Buscar automóviles" + " "*27 + "║")
        print("║  3. Buscar bicicletas" + " "*28 + "║")
        print("║  4. Regresar al menú principal" + " "*19 + "║")
        print("="*50)
        opc = input("➤ Digite una opción: ")
        
        if opc == "1":  
            b_placa = input("🏍️  Ingrese la placa de la moto: ").upper()
            if len(b_placa) != 6 or not b_placa[:3].isalpha() or not b_placa[3:5].isdigit() or not b_placa[5].isalpha():
                print("❌ Formato de placa inválido para moto (debe ser 3 letras + 2 números + 1 letra)")
                continue
            
            encontrado = False
            for registro in lregistro:
                if registro.get('Num Placa') == b_placa and registro.get('Vehiculo tipo') == "Moto":
                    print("\n" + "="*50)
                    print("║" + " "*13 + "✅ VEHÍCULO ENCONTRADO" + " "*15 + "║")
                    print("="*50)
                    for clave, valor in registro.items():
                        if clave != 'h' and clave != 'm' and clave != 's':
                            print(f"║  {clave}: {valor}")
                    print("="*50)
                    encontrado = True
                    break
            
            if not encontrado:
                print("\n❌ Moto no encontrada en el sistema")
            
            input("\n⏎ Presiona Enter para continuar...")
                    
        elif opc == "2":  
            b_placa = input("🚗 Ingrese la placa del automóvil: ").upper()
            if len(b_placa) != 6 or not b_placa[:3].isalpha() or not b_placa[3:].isdigit():
                print("❌ Formato de placa inválido para automóvil (debe ser 3 letras + 3 números)")
                continue
            
            encontrado = False
            for registro in lregistro:
                if registro.get('Num Placa') == b_placa and registro.get('Vehiculo tipo') == "Auto":
                    print("\n" + "="*50)
                    print("║" + " "*13 + "✅ VEHÍCULO ENCONTRADO" + " "*15 + "║")
                    print("="*50)
                    for clave, valor in registro.items():
                        if clave != 'h' and clave != 'm'and clave != 's':
                            print(f"║  {clave}: {valor}")
                    print("="*50)
                    encontrado = True
                    break
            
            if not encontrado:
                print("\n❌ Automóvil no encontrado en el sistema")
            
            input("\n⏎ Presiona Enter para continuar...")
                
        elif opc == "3":  
            try:
                b_consecutivo = int(input("🚲 Ingrese el número consecutivo de la bicicleta: "))
            except ValueError:
                print("❌ Debe ingresar un número válido")
                continue
            
            encontrado = False
            for registro in lregistro:
                if registro.get('Consecutivo') == b_consecutivo and registro.get('Vehiculo tipo') == "Bicicleta":
                    print("\n" + "="*50)
                    print("║" + " "*13 + "✅ VEHÍCULO ENCONTRADO" + " "*15 + "║")
                    print("="*50)
                    for clave, valor in registro.items():
                        if clave != 'h' and clave != 'm':
                            print(f"║  {clave}: {valor}")
                    print("="*50)
                    encontrado = True
                    break
            
            if not encontrado:
                print("\n❌ Bicicleta no encontrada en el sistema")
            
            input("\n⏎ Presiona Enter para continuar...")
                
        elif opc == "4":
            break
        else:
            print("\n❌ Opción inválida. Por favor intente nuevamente.")
                    

def buscar_registro(lregistro):
    while True:
        print("\n" + "="*50)
        print("║" + " "*15 + "BUSCAR REGISTRO" + " "*20 + "║")
        print("="*50)
        print("║  1. Mostrar todos los automóviles" + " "*15 + "║")
        print("║  2. Mostrar todas las motocicletas" + " "*15 + "║")
        print("║  3. Mostrar todas las bicicletas" + " "*17 + "║")
        print("║  4. Regresar al menú principal" + " "*19 + "║")
        print("="*50)
        opc = input("➤ Digite una opción: ")
        encontrado = False
        if opc == "1":
            print("\n" + "="*120)
            print("🚗 AUTOMÓVILES REGISTRADOS".center(120))
            print("="*120)
            print(f"{'FACTURA':<10} {'PLACA':<10} {'FECHA':<12} {'INGRESO':<10} {'SALIDA':<10} {'MINUTOS':<10} {'TOTAL':<10} {'MENSUALIDAD':<15}")
            print("-"*120)
            encontrado = False
            for registro in lregistro:
                if registro.get('Vehiculo tipo') == "Auto":
                    encontrado = True
                    factura = registro.get('Factura No')
                    placa = registro.get('Num Placa')
                    fecha = registro.get('Fecha de ingreso')
                    ingreso = registro.get('Hora de ingreso')
                    salida = registro.get('Hora de salida', '')
                    minutos = registro.get('Numero minutos', '')
                    total = registro.get('Total', '')
                    me = registro.get('Mensualidad', '')
                    print(f"{factura:<10} {placa:<10} {fecha:<12} {ingreso:<10} {salida:<10} {minutos:<10} {total:<10} {me:<15}")
            print("="*120)
            if not encontrado:
                    print("❌ No hay registros de este vehículo".center(120))
            input("\n⏎ Presiona Enter para continuar...")
        elif opc == "2":
            print("\n" + "="*120)
            print("🏍️  MOTOCICLETAS REGISTRADAS".center(120))
            print("="*120)
            print(f"{'FACTURA':<10} {'PLACA':<10} {'FECHA':<12} {'INGRESO':<10} {'SALIDA':<10} {'MINUTOS':<10} {'TOTAL':<10}")
            print("-"*120)
            for registro in lregistro:
                if registro.get('Vehiculo tipo') == "Moto":
                    encontrado = True
                    factura = registro.get('Factura No')
                    placa = registro.get('Num Placa')
                    fecha = registro.get('Fecha de ingreso')
                    ingreso = registro.get('Hora de ingreso')
                    salida = registro.get('Hora de salida', '')
                    minutos = registro.get('Numero minutos', '')
                    total = registro.get('Total', '')
                    me = registro.get('Mensualidad', '')
                    print(F"{factura:<10} {placa:<10} {fecha:<12} {ingreso:<10} {salida:<10} {minutos:<10} {total:<10}")
            print("="*120)
            if not encontrado:
                print("❌ No hay registros de este vehículo".center(120))
            input("\n⏎ Presiona Enter para continuar...")
        elif opc == "3":
            print("\n" + "="*120)
            print("🚲 BICICLETAS REGISTRADAS".center(120))
            print("="*120)
            print(f"{'FACTURA':<10} {'CONSECUTIVO':<15} {'FECHA':<12} {'INGRESO':<10} {'SALIDA':<10} {'MINUTOS':<10} {'TOTAL':<10}")
            print("-"*120)
            for registro in lregistro:
                if registro.get('Vehiculo tipo') == 'Bicicleta':
                    encontrado = True
                    factura = registro.get('Factura No')
                    con = registro.get('Consecutivo')
                    fecha = registro.get('Fecha de ingreso')
                    ingreso = registro.get('Hora de ingreso')
                    salida = registro.get('Hora de salida')
                    minutos = registro.get('Numero minutos', '')
                    total = registro.get('Total', '')
                    print(f"{factura:<10} {con:<15} {fecha:<12} {ingreso:<10} {salida:<10} {minutos:<10} {total:<10}")
            print("="*120)
            if not encontrado:
                print("❌ No hay registros de este vehículo".center(120))
            input("\n⏎ Presiona Enter para continuar...")
        elif opc == "4":
            break

        else:
            print("\n❌ Opción inválida. Por favor intente nuevamente.")



def mostrar_mensualidad(mensualidadl):
    encontrado = False
    print("\n" + "="*100)
    print("📅 MENSUALIDADES REGISTRADAS".center(100))
    print("="*100)
    print(f"{'MENSUALIDAD':<15} {'NO.PLACA':<12} {'CLIENTE':<20} {'DESDE':<15} {'HASTA':<15} {'TOTAL':<10}")
    print("-"*100)
    for me in mensualidadl:
        encontrado = True
        mostrar_m1 = me.get('Factura No')
        mostrar_m2 = me.get('Num Placa del auto')
        mostrar_m3 = me.get('Nombre')
        mostrar_m4 = me.get('Fecha ingreso')
        mostrar_m5 = me.get('Vigencia hasta')
        mostrar_m6 = me.get('Total')

        print(f"{mostrar_m1:<15} {mostrar_m2:<12} {mostrar_m3:<20} {str(mostrar_m4):<15} {str(mostrar_m5):<15} ${mostrar_m6:<9}")
    print("="*100)

    if not encontrado:
        print("❌ No hay mensualidades registradas".center(100))
    
    input("\n⏎ Presione Enter para continuar...")


def salida_vehiculo(lregistro, t_auto, t_moto, t_bici):
    while True:
        print("\n" + "="*50)
        print("║" + " "*14 + "REGISTRAR SALIDA" + " "*20 + "║")
        print("="*50)
        tipo = input("🚗 Tipo de vehículo (a: automóvil, m: moto, b: bicicleta): ").lower()
        if tipo != "a" and tipo != "m" and tipo != "b":
            print("❌ Tipo de vehículo inválido")
            continue
        
        encontrado = False
        
        if tipo == "a" or tipo == "m":
            s_placa = input("🔢 Digite su número de placa (auto: 3 letras + 3 números, moto: 3 letras + 2 números + 1 letra): ").upper()
            if tipo == "a":
                if len(s_placa) != 6 or not s_placa[:3].isalpha() or not s_placa[3:].isdigit():
                    print("❌ Formato de placa inválido para automóvil (debe ser 3 letras + 3 números)")
                    continue
            if tipo == "m":
                if len(s_placa) != 6 or not s_placa[:3].isalpha() or not s_placa[3:5].isdigit() or not s_placa[5].isalpha():
                    print("❌ Formato de placa inválido para moto (debe ser 3 letras + 2 números + 1 letra)")
                    continue
            
            for registro in lregistro:
                if registro.get('Num Placa') == s_placa and registro.get('s') == "sin salida":
                    encontrado = True
                    h = registro.get('h')
                    m = registro.get('m')
                    break
            if not encontrado:
                print("\n❌ Vehículo no encontrado")
                print("❌ O ya registró salida")
                continue

        
        if tipo == "b":
            try:
                const = int(input("🚲 Digite el consecutivo: "))
                for registro in lregistro:
                    if registro.get('Consecutivo') == const and registro.get('s') == "sin salida":
                        encontrado = True
                        h = registro.get('h')
                        m = registro.get('m')
                        break
                if not encontrado:
                    print("\n❌ Bicicleta no encontrada")
                    print("❌ O ya registró salida")
                    continue
                
            except ValueError:
                print("❌ Debe ingresar un número válido")
                continue
        
        try:
            hora_salida = int(input("🕐 Digite la hora de salida (formato 24 horas: hhmm): "))
            hora = hora_salida // 100
            minuts = hora_salida % 100
            if hora < 0 or hora > 23 or minuts < 0 or minuts > 59:
                print("❌ Hora inválida (hora debe estar entre 00-23 y minutos entre 00-59)")
                continue    
        except ValueError:
            print("❌ Opción inválida")
            continue 

        if h > hora or (h == hora and m > minuts):
            print("❌ La hora de salida debe ser mayor a la hora de ingreso")
            continue
        
        if tipo == "a":
            for registro in lregistro:
                if registro.get('Vehiculo tipo') == "Auto" and registro.get('Num Placa') == s_placa:
                    registro['Hora de salida'] = hora_salida

                    if registro.get("Mensualidad") == "vigente":
                        t_auto = 0
                    
                    if m <= minuts:
                        hora_t = hora - h
                        hora_t = hora_t * 60
                        minutos_t = minuts - m
                        minuts = minutos_t + hora_t
                    else:
                        h += 1
                        hora_t = (hora - h) * 60
                        minutos_t = minuts + m
                        minuts = minutos_t + hora_t
                    
                    t = minuts * t_auto
                    registro['Numero minutos'] = minuts
                    registro['Total'] = t
                    registro['s'] = "con salida"
                    break

        if tipo == "m":
            for registro in lregistro:
                if registro.get('Vehiculo tipo') == 'Moto' and registro.get('Num Placa') == s_placa:
                    registro['Hora de salida'] = hora_salida
                    
                    if m <= minuts:
                        hora_t = hora - h
                        hora_t = hora_t * 60
                        minutos_t = minuts - m
                        minuts = minutos_t + hora_t
                    else:
                        h += 1
                        hora_t = (hora - h) * 60
                        minutos_t = minuts + m
                        minuts = minutos_t + hora_t
                    
                    t = minuts * t_moto
                    registro['Numero minutos'] = minuts
                    registro['Total'] = t
                    registro['s'] = "con salida"
                    break
        
        if tipo == "b":
            for registro in lregistro:
                if registro.get('Vehiculo tipo') == 'Bicicleta' and registro.get('Consecutivo') == const:
                    registro['Hora de salida'] = hora_salida
                    
                    if m <= minuts:
                        hora_t = hora - h
                        hora_t = hora_t * 60
                        minutos_t = minuts - m
                        minuts = minutos_t + hora_t
                    else:
                        h += 1
                        hora_t = (hora - h) * 60
                        minutos_t = minuts + m
                        minuts = minutos_t + hora_t
                    
                    t = minuts * t_bici
                    registro['Numero minutos'] = minuts
                    registro['Total'] = t
                    registro['s'] = "con salida"
                    break
        
        print("\n" + "="*50)
        print("║" + " "*13 + "✅ SALIDA REGISTRADA" + " "*17 + "║")
        print("="*50)
        break
    
    return lregistro

def buscar_factura (lregistro):
    encontrado = False
    while True:
        try:
            fac = int(input("🔍 Digite el número de su factura: "))
            for registro in lregistro:
                if registro.get('Factura No') == fac :
                    print("\n" + "="*50)
                    print("║" + " "*13 + "✅ FACTURA ENCONTRADA" + " "*16 + "║")
                    print("="*50)
                    for clave, valor in registro.items():
                        if clave != 'h' and clave != 'm' and clave != 's':
                            print(f"║  {clave}: {valor}")
                    print("="*50)
                    encontrado = True
                    break
            
            if not encontrado:
                print("\n❌ Factura no encontrada en el sistema")
            
            input("\n⏎ Presiona Enter para continuar...")
            break
        except ValueError:
            print("❌ Opción inválida. Debe ingresar un número")
            continue

def cuadre_caja(lregistro, mensualidadl):
    print("\n" + "="*50)
    print("║" + " "*16 + "CUADRE DE CAJA" + " "*20 + "║")
    print("="*50)
    
    total_vehiculos = 0
    
    for registro in lregistro:
        if registro.get('s') == "con salida":
            total = registro.get('Total', 0)
            total_vehiculos += total
    
    total_mensualidades = 0
    
    for mensualidad in mensualidadl:
        total = mensualidad.get('Total', 0)
        total_mensualidades += total
    
    print(f"║  💰 Total vehículos con salida:       ${total_vehiculos:<10}║")
    print(f"║  📅 Total mensualidades registradas:  ${total_mensualidades:<10}║")
    print("-"*50)
    total_general = total_vehiculos + total_mensualidades
    print(f"║  💵 TOTAL GENERAL:                    ${total_general:<10}║")
    print("="*50)
    
    input("\n⏎ Presione Enter para continuar...")

def inicio ():
    mensualidadl = []
    lregistro = []
    fac_registro = 0
    lplacas = []
    consecutivo = 202500
    lmensualidad = []
    numero_factura = 1
    t_auto = 0
    t_moto = 0
    t_bici = 0
    mensualidad = 0

    while True:
        print("\n" + "="*50)
        print("║" + " "*10 + "🅿️  SISTEMA DE ESTACIONAMIENTO" + " "*10 + "║")
        print("="*50)
        print("║  1.  Tarifas" + " "*37 + "║")
        print("║  2.  Registrar mensualidad" + " "*23 + "║")
        print("║  3.  Ingresar vehículo" + " "*27 + "║")
        print("║  4.  Buscar vehículo" + " "*29 + "║")
        print("║  5.  Mostrar registros" + " "*27 + "║")
        print("║  6.  Mostrar Mensualidades" + " "*23 + "║")
        print("║  7.  Salida vehículo" + " "*29 + "║")
        print("║  8.  Buscar Factura" + " "*30 + "║")
        print("║  9.  Cuadre de Caja" + " "*30 + "║")
        print("║  10. Salir" + " "*39 + "║")
        print("="*50)
        opc = input("➤ Digite una opción: ")

        if opc == "1":
            t_auto,t_moto,t_bici,mensualidad = tarifa(t_auto,t_moto,t_bici,mensualidad)
        elif opc == "2":
            numero_factura, lmensualidad, mensualidadl = registrar_mensualidad(mensualidad,numero_factura,lmensualidad,mensualidadl)
        elif opc == "3":
           lplacas, fac_registro, consecutivo, lregistro = ingresar_vehiculo(lregistro,fac_registro,lplacas,consecutivo,lmensualidad)
        elif opc == "4":
            buscar_vehiculo(lregistro)
        elif opc == "5":
            buscar_registro(lregistro)
        elif opc == "6":
            mostrar_mensualidad(mensualidadl)
        elif opc == "7":
            lregistro = salida_vehiculo(lregistro, t_auto, t_moto, t_bici)
        elif opc == "8":
            buscar_factura(lregistro)
        elif opc == "9":
            cuadre_caja(lregistro, mensualidadl)
        elif opc == "10":
            print("\n" + "="*50)
            print("║" + " "*8 + "👋 Gracias por usar el sistema" + " "*11 + "║")
            print("="*50)
            break
        else:
            print("\n❌ Opción inválida. Por favor intente nuevamente.")

inicio()