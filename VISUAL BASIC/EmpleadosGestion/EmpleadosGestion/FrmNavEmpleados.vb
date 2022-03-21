Imports System.Data.OleDb



Public Class FrmNavEmpleados

    'conexion
    Dim oConexion As New OleDbConnection
    'Dim oDataAdapter As OleDbDataAdapter, lleva la select
    Dim oDataAdapter As New OleDbDataAdapter("Select * from empleados", oConexion)
    'traductor
    Dim oCommandBuilder = New OleDbCommandBuilder(oDataAdapter)
    'copia exacta de la bbdd
    Dim oDataSet As New DataSet
    'posicion es el nº de la fila con la que queremos interactuar
    Dim Posicion As Integer


    'Dim oDataRow As DataRow


    'MIRAR de que manera esta linkado a la hora de cambiarle el nombre al Form1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    'lleva la conexion a la bbdd
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles Me.Load

        Dim resultado As Integer
        resultado = MessageBox.Show("Mostrar datos?", "Datos personales", MessageBoxButtons.YesNo, MessageBoxIcon.Question)
        MessageBox.Show("Nivel administrativo: " & Module1.nivel)

        If resultado = vbYes Then

            GrupoDatos.Visible = True

            'Cargamos el color de fondo que hayamos escogido
            Me.BackColor = Module1.FormBackgroundColor
            Me.ForeColor = Module1.FormTextColor

            oConexion.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=zoologico.mdb"
            oConexion.Open()

            oDataAdapter.Fill(oDataSet, "empleados")
            oConexion.Close()
            Posicion = 0
            Cargar()


        Else
            Close()
        End If

        Comprobacion_Nivel_Administrativo()


    End Sub


    'Carga los datos de la bbdd
    Private Sub Cargar()

        Try

            If oDataSet.Tables("empleados").Rows.Count = 0 Then
                MessageBox.Show("No hay ningún registro", "AVISO")
            Else
                Dim odatarow = oDataSet.Tables("empleados").Rows(Posicion)
                txtNombre.Text = odatarow("nombre")
                txtApellido1.Text = odatarow("apellido1")
                txtApellido2.Text = odatarow("apellido2")
                txtCorreo.Text = odatarow("correo")
                txtContra.Text = odatarow("contrasenna")
                txtSueldo.Text = odatarow("sueldo")
                txtNivel.Text = odatarow("nivel_administrativo")
                txtFKzoo.Text = odatarow("fk_zoo")

                lblRegistros.Text = "Registro" & Posicion + 1 & " de " & oDataSet.Tables("empleados").Rows.Count
            End If

        Catch ex As Exception
            btnSiguiente.Enabled = False
            btnAnterior.Enabled = False
            btnUltimo.Enabled = False
            btnPrimero.Enabled = False
        End Try

    End Sub




    '-------- BTNS GROUP BOX NAVEGACION --------
    Private Sub CambiarBotones(valor1 As Boolean, valor2 As Boolean, valor3 As Boolean, valor4 As Boolean)
        btnSiguiente.Enabled = valor1
        btnAnterior.Enabled = valor2
        btnPrimero.Enabled = valor3
        btnUltimo.Enabled = valor4
    End Sub

    Private Sub btnSiguiente_Click(sender As Object, e As EventArgs) Handles btnSiguiente.Click
        Posicion += 1
        btnAnterior.Enabled = True

        If oDataSet.Tables("empleados").Rows.Count - 1 = Posicion Then CambiarBotones(False, True, True, False)
        Cargar()
    End Sub

    Private Sub btnAnterior_Click(sender As Object, e As EventArgs) Handles btnAnterior.Click
        Posicion -= 1
        btnSiguiente.Enabled = True

        If Posicion = 0 Then CambiarBotones(True, False, False, True)
        Cargar()
    End Sub

    Private Sub btnPrimero_Click(sender As Object, e As EventArgs) Handles btnPrimero.Click
        Posicion = 0
        btnPrimero.Enabled = True
        If Posicion = 0 Then CambiarBotones(True, False, False, True)
        Cargar()
    End Sub

    Private Sub btnUltimo_Click(sender As Object, e As EventArgs) Handles btnUltimo.Click
        Posicion = oDataSet.Tables("empleados").Rows.Count - 1
        btnUltimo.Enabled = False
        If oDataSet.Tables("empleados").Rows.Count - 1 = Posicion Then CambiarBotones(False, True, True, False)
        Cargar()
    End Sub

    Private Sub btnLimpiarCampos_Click(sender As Object, e As EventArgs) Handles btnLimpiarCampos.Click
        txtNombre.Text = ""
        txtApellido1.Text = ""
        txtApellido2.Text = ""
        txtCorreo.Text = ""
        txtContra.Text = ""
        txtSueldo.Text = ""
        txtNivel.Text = ""
        lblRegistros.Text = ""
    End Sub






    '-------- BTNS GROUP BOX MANTENIMIENTO --------
    Private Sub btnInsertar_Click(sender As Object, e As EventArgs) Handles btnInsertar.Click
        Dim oDataRow As DataRow
        oDataRow = oDataSet.Tables("empleados").NewRow()
        oDataRow("nombre") = txtNombre.Text
        oDataRow("apellido1") = txtApellido1.Text
        oDataRow("apellido2") = txtApellido2.Text
        oDataRow("correo") = txtCorreo.Text
        oDataRow("contrasenna") = txtContra.Text
        oDataRow("sueldo") = txtSueldo.Text
        oDataRow("nivel_administrativo") = txtNivel.Text
        oDataRow("fk_zoo") = txtFKzoo.Text

        oDataSet.Tables("empleados").Rows.Add(oDataRow)
        Posicion = 0
        Cargar()
    End Sub

    Private Sub btnModificar_Click(sender As Object, e As EventArgs) Handles btnModificar.Click
        Dim oDataRow As DataRow
        'accedemos al metodo de rows para que devuelva las filas que tienen en comun en la posicion
        'devuelve las filas que coincide con posicion
        'recoge las filas que coincide con posicion
        oDataRow = oDataSet.Tables("empleados").Rows(Posicion)
        oDataRow("nombre") = txtNombre.Text
        oDataRow("apellido1") = txtApellido1.Text
        oDataRow("apellido2") = txtApellido2.Text
        oDataRow("correo") = txtCorreo.Text
        oDataRow("contrasenna") = txtContra.Text
        oDataRow("sueldo") = txtSueldo.Text
        oDataRow("nivel_administrativo") = txtNivel.Text
        oDataRow("fk_zoo") = txtFKzoo.Text
        Cargar()
    End Sub

    Private Sub btnActualizar_Click(sender As Object, e As EventArgs) Handles btnActualizar.Click
        oDataAdapter.Update(oDataSet, "empleados")
        Cargar()
        MessageBox.Show("Se ha actualizado los registros", "AVISO")
    End Sub

    Private Sub btnBorrar_Click(sender As Object, e As EventArgs) Handles btnBorrar.Click
        Dim oDataRow As DataRow
        oDataRow = oDataSet.Tables("empleados").Rows(Posicion)
        oDataRow.Delete()

        Dim oTablaBorrada As DataTable
        oTablaBorrada = oDataSet.Tables("empleados").GetChanges(DataRowState.Deleted)

        'oDataAdapter = New OleDbDataAdapter("Select * from empleados", oConexion)
        'oDataAdapter = New OleDbDataAdapter("Select * from empleados", oConexion)
        oDataAdapter.Update(oTablaBorrada)
        'oDataAdapter = Nothing
        oDataSet.Tables("empleados").AcceptChanges()
        'como dice guille simula un click a si mismo 
        btnPrimero.PerformClick()
    End Sub

    Private Sub btnDeleteAllRows_Click(sender As Object, e As EventArgs) Handles btnDeleteAllRows.Click
        Dim oDataRow As DataRow
        For Each oDataRow In oDataSet.Tables("empleados").Rows
            oDataRow.Delete()
            '   Cargar()
        Next

        Dim oTablaBorrada As DataTable
        oTablaBorrada = oDataSet.Tables("empleados").GetChanges(DataRowState.Deleted)
        oDataSet.Tables("empleados").AcceptChanges()
        Cargar()
        btnLimpiarCampos.PerformClick()
        lblRegistros.Text = "No existen filas"
    End Sub





    'ESTOS 2 HAY QUE REVISARLOS
    'Private Sub FrmNaveBBDD_Closed(sender As Object, e As EventArgs) Handles Me.Closed
    '    'InicioFrm.BtnBBDD.Enabled = True
    'End Sub


    '-------- BTNS GROUP BOX MANTENIMIENTO --------
    Private Sub btnBuscar_Click(sender As Object, e As EventArgs) Handles btnBuscar.Click

        Try
            Dim oDataRow As DataRow()
            'Dim expression = "Dni = '" & TxtDNIBuscar.Text & "'"
            Dim expression = "id_empleado =" & txtBuscarNivel.Text
            oDataRow = oDataSet.Tables("empleados").Select(expression)

            Dim oTabla As New DataTable
            oTabla = oDataRow.CopyToDataTable
            DataGridDatos.DataSource = oTabla

        Catch ex As Exception
            MessageBox.Show("Busque un id válido")
        End Try

    End Sub


    '-------- COMPROBACION DE NIVEL DEL USUARIO --------
    Private Sub Comprobacion_Nivel_Administrativo()

        If Module1.nivel.Equals("estandar") Then
            btnInsertar.Enabled = False
            btnActualizar.Enabled = False
            btnBorrar.Enabled = False
            btnDeleteAllRows.Enabled = False
            btnModificar.Enabled = False
            btnLimpiarCampos.Enabled = False
            txtNivel.Enabled = False
            txtNombre.Enabled = False
            txtApellido1.Enabled = False
            txtApellido2.Enabled = False
            txtSueldo.Enabled = False
            txtFKzoo.Enabled = False
        End If


        If Module1.nivel.Equals("avanzado") Then
            btnBorrar.Enabled = False
            btnDeleteAllRows.Enabled = False
            txtNivel.Enabled = False
        End If

    End Sub
End Class
