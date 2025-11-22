from flask import Flask, render_template, request

app = Flask(__name__)

# menu
@app.route("/")
def home():
    return render_template("index.html")

# Ejercicio 1
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        edad_str = request.form.get("edad", "").strip()
        tarros_str = request.form.get("tarros", "").strip()

        errores = []
        if not nombre:
            errores.append("El nombre es obligatorio.")
        try:
            edad = int(edad_str)
            if edad < 0:
                errores.append("La edad no puede ser negativa.")
        except ValueError:
            errores.append("La edad debe ser un número entero.")

        try:
            tarros = int(tarros_str)
            if tarros <= 0:
                errores.append("La cantidad de tarros debe ser un entero positivo.")
        except ValueError:
            errores.append("La cantidad de tarros debe ser un número entero.")

        if errores:
            return render_template("ejercicio1.html", errores=errores, form=request.form)

        precio_por_tarro = 9000
        total_sin_descuento = tarros * precio_por_tarro

        if 18 <= edad <= 30:
            descuento_pct = 0.15
        elif edad > 30:
            descuento_pct = 0.25
        else:
            descuento_pct = 0.0

        monto_descuento = total_sin_descuento * descuento_pct
        total_con_descuento = total_sin_descuento - monto_descuento

        return render_template(
            "ejercicio1_resultado.html",
            nombre=nombre,
            edad=edad,
            tarros=tarros,
            precio_por_tarro=precio_por_tarro,
            total_sin_descuento=total_sin_descuento,
            descuento_pct=int(descuento_pct * 100),
            monto_descuento=monto_descuento,
            total_con_descuento=total_con_descuento,
        )


    return render_template("ejercicio1.html", form={})

# Ejercicio 2: Login
USUARIOS = {
    "juan": {"password": "admin", "rol": "administrador"},
    "pepe": {"password": "user", "rol": "usuario"},
}

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        password = request.form.get("password", "").strip()

        registro = USUARIOS.get(usuario)
        if registro and password == registro["password"]:
            mensaje = f"Bienvenido {registro['rol']} {usuario}"
            return render_template("ejercicio2_resultado.html", ok=True, mensaje=mensaje)
        else:
            mensaje = "Usuario y/o contraseña incorrectos"
            return render_template("ejercicio2_resultado.html", ok=False, mensaje=mensaje)

    # GET
    return render_template("ejercicio2.html")

if __name__ == "__main__":
    app.run(debug=True)
