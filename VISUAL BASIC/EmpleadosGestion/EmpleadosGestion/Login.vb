Imports System.Data.OleDb
Imports System.IO
Imports System.Security.Cryptography
Imports System.Text

Public Class Login
    'Variable que recoge el nivel de acceso del empleado que inicia sesion
    Dim _nivel As String = Nothing
    'id del empleado que inicia sesion
    Dim _id As Integer = 0
    'Nombre del empleado que inicia sesion
    Dim _nombre As String


    Private Sub BtnLogin_Click(sender As Object, e As EventArgs) Handles BtnLogin.Click
        Dim oConexion As New OleDbConnection
        'Dim oDataAdapter As OleDbDataAdapter, lleva la instruccion sql que queremos ejecutar
        Dim oDataAdapter As New OleDbDataAdapter("SELECT * FROM empleados WHERE correo like '" & txtCorreo.Text & "' AND contrasenna like '" & txtContra.Text & "';", oConexion)
        'traductor
        Dim oCommandBuilder = New OleDbCommandBuilder(oDataAdapter)
        'variable donde se hara una copia de la base de datos
        Dim oDataSet As New DataSet


        oConexion.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=zoologico.mdb"
        oConexion.Open()
        'llenamos nuestro dataset con los datos de nuestra base de datos
        oDataAdapter.Fill(oDataSet, "empleados")


        If oDataSet.Tables("empleados").Rows.Count > 0 Then
            'Asignamos las varibales del usuario que se ha introducido
            _nivel = oDataSet.Tables("empleados").Rows(0).Item(7).ToString()
            _id = oDataSet.Tables("empleados").Rows(0).Item(0).ToString()
            _nombre = oDataSet.Tables("empleados").Rows(0).Item(1).ToString()

            Module1.nivel = _nivel
            Module1.id_usuario = _id
            Module1.nombre_usuario = _nombre

            'InicioFrm.GetSetID = id
            'NavEmpleadosBBDFrm.GetSetNivel = _nivel
            'NavEmpleadosBBDFrm.GetSetID = id

            'llamar al metodo de ficheros
            Leer_Fichero()


            InicioFrm.Show()
            Me.Hide()
        End If
    End Sub




    '------------------------------------------------ FICHEROS -----------------------------------------------
    Private Sub BtnGrabar_Click(sender As Object, e As EventArgs) Handles BtnGrabar.Click
        Dim oConexion As New OleDbConnection
        Dim oDataSet As New DataSet

        Dim Escribir As New StreamWriter("C:\vb\Users_ModoClaroOscuro.txt", True) 'si el archivo existe se añade y si no se crea
        Module1.id_usuario = Module1.id_usuario

        'CONEXION
        Dim oDataAdapter As New OleDbDataAdapter("SELECT * FROM empleados WHERE correo like '" & txtCorreo.Text & "' AND contrasenna like '" & txtContra.Text & "';", oConexion)
        Dim oCommandBuilder = New OleDbCommandBuilder(oDataAdapter)


        oConexion.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=zoologico.mdb"
        oConexion.Open()
        oDataAdapter.Fill(oDataSet, "empleados")

        If oDataSet.Tables("empleados").Rows.Count > 0 Then
            Module1.id_usuario = oDataSet.Tables("empleados").Rows(0).Item(0).ToString()
            Module1.nivel = oDataSet.Tables("empleados").Rows(0).Item(7).ToString()

            'MessageBox.Show("El usuario con id: " & id & " tiene acceso de: " & _nivel)
        End If
        oConexion.Close()



        If ChkOscuro.Checked = True Then
            Escribir.Write(Module1.id_usuario & "o" & ";")
        Else
            Escribir.Write(Module1.id_usuario & "c" & ";")
        End If
        'MessageBox.Show(id)
        Escribir.Close()

        MessageBox.Show("Se han guardado los cambios", "AVISO")
    End Sub

    Private Sub Leer_Fichero()

        Try
            Dim oConexion As New OleDbConnection
            Dim oDataSet As New DataSet
            'CONEXION
            Dim oDataAdapter As New OleDbDataAdapter("SELECT * FROM empleados WHERE correo like '" & txtCorreo.Text & "' AND contrasenna like '" & txtContra.Text & "';", oConexion)
            Dim oCommandBuilder = New OleDbCommandBuilder(oDataAdapter)


            oConexion.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=zoologico.mdb"
            oConexion.Open()
            oDataAdapter.Fill(oDataSet, "empleados")

            If oDataSet.Tables("empleados").Rows.Count > 0 Then
                Module1.id_usuario = oDataSet.Tables("empleados").Rows(0).Item(0).ToString()
                Module1.nivel = oDataSet.Tables("empleados").Rows(0).Item(8).ToString()
                'MessageBox.Show("El usuario con id: " & id & " tiene acceso de: " & _nivel)
            End If

            oConexion.Close()

            Dim Leer As New StreamReader("C:\vb\Users_ModoClaroOscuro.txt", True)
            Dim CarLeido As Integer
            'CarLeido = Leer.Read
            Dim configuracion As Char
            Dim experimento As Boolean = True


            'cuando encuetra el id ya no tiene sentido esta en el do while entonces
            'ya noe ntra en el while
            Do While Not (CarLeido = -1) And (experimento = True)
                'Usuario
                Do While Not (Chr(CarLeido) = "-1")
                    Dim id_char As Integer = Module1.id_usuario

                    If (Chr(CarLeido) = ("" & id_char & "")) Then
                        CarLeido = Leer.Read
                        configuracion = Chr(CarLeido)
                        experimento = False
                        'MessageBox.Show(Chr(CarLeido))
                        Exit Do
                    End If
                    'txtCorreo.Text = txtCorreo.Text & Chr(CarLeido)
                    CarLeido = Leer.Read
                    'MessageBox.Show(Chr(CarLeido))

                Loop

                If configuracion = "o" Then
                    If ChkOscuro.Checked = True Then
                        MessageBox.Show("oscuro")
                    Else
                        ChkOscuro.Checked = True
                    End If
                Else
                    ChkOscuro.Checked = False
                    MessageBox.Show("claro")
                End If
                txtCorreo.Text = ""
            Loop

            'MessageBox.Show("Final archivo")
            Leer.Close()

        Catch ex As Exception
            MessageBox.Show("No has guardado la configuración")
        End Try


    End Sub


    Private Sub ChkOscuro_CheckedChanged(sender As Object, e As EventArgs) Handles ChkOscuro.CheckedChanged
        If ChkOscuro.Checked Then
            Me.ForeColor = Color.White
            Me.BackColor = Color.Gray
        End If
        If ChkOscuro.Checked = False Then
            Me.BackColor = Color.WhiteSmoke
            Me.ForeColor = Color.Black
        End If

    End Sub
End Class
