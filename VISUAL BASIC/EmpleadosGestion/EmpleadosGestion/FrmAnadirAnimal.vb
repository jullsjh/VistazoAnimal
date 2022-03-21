Imports System.Data.OleDb

Public Class FrmAnadirAnimal

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
    Dim i As Integer
    Dim id_habitat As Integer
    Dim id_especie As Integer


    Private Sub Frm_AnnadirAnimal_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

        'Cargamos el color de fondo que hayamos escogido
        Me.BackColor = Module1.FormBackgroundColor
        Me.ForeColor = Module1.FormTextColor

        'GrupoDatos.Visible = True

        'Cargamos el color de fondo que hayamos escogido
        Me.BackColor = Module1.FormBackgroundColor
        Me.ForeColor = Module1.FormTextColor

        oConexion.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=zoologico.mdb"
        oConexion.Open()

        oDataAdapter = New OleDbDataAdapter("select * from animales", oConexion)
        oCommandBuilder = New OleDbCommandBuilder(oDataAdapter)
        'llenamos el dataset con la tabla de animales
        oDataAdapter.Fill(oDataSet, "animales")

        oDataAdapter = New OleDbDataAdapter("select * from habitat", oConexion)
        oCommandBuilder = New OleDbCommandBuilder(oDataAdapter)
        'llenamos el dataset con la tabla de habitat
        oDataAdapter.Fill(oDataSet, "habitat")

        oDataAdapter = New OleDbDataAdapter("select * from especies", oConexion)
        oCommandBuilder = New OleDbCommandBuilder(oDataAdapter)
        'llenamos el dataset con la tabla de especie
        oDataAdapter.Fill(oDataSet, "especies")

        cmbHabitat_CargarDatos()
        cmbEspecie_CargarDatos()
        oConexion.Close()


        'For i = 0 To oDataSet.Tables.Count - 1
        '    cmbEspecie.Items.Add(oDataSet.Tables.Item(i))
        'Next

        'For i = 0 To oDataSet.Tables.Count - 1
        '    cmbHabitat.Items.Add(oDataSet.Tables.Item(i))
        'Next




        Posicion = 0
        Cargar()

    End Sub



    Private Sub Cargar()

        Try

            If oDataSet.Tables("animales").Rows.Count = 0 Then
                MessageBox.Show("No hay ningún registro", "AVISO")
            Else
                Dim odatarow = oDataSet.Tables("animales").Rows(Posicion)
                txtNombreAnimal.Text = odatarow("nombre_animal")
                txtTamanno.Text = odatarow("tamanno")
                txtPeso.Text = odatarow("peso")

                lblRegistros.Text = "Registro " & Posicion + 1 & " de " & oDataSet.Tables("animales").Rows.Count

            End If

        Catch ex As Exception
            btnSiguiente.Enabled = False
            btnAnterior.Enabled = False
            btnUltimo.Enabled = False
            btnPrincipio.Enabled = False
        End Try





    End Sub


    '-------- LLENAR LAS COMBOBOX CON LOS CAMPOS --------
    Private Sub cmbHabitat_CargarDatos()
        Try
            cmbHabitat.Text = "Habitats del zoologico"


            Dim resultado As Integer
            resultado = oDataSet.Tables("habitat").Rows.Count()


            For i = 0 To resultado - 1
                cmbHabitat.Items.Add(oDataSet.Tables("habitat").Rows(i).Item(1).ToString())
            Next


        Catch ex As Exception
            MessageBox.Show("No existen datos dentro de esta tabla")
        End Try
    End Sub


    Private Sub cmbEspecie_CargarDatos()
        Try
            cmbEspecie.Text = "Especies del zoologico"


            Dim resultado As Integer
            resultado = oDataSet.Tables("especies").Rows.Count()


            For i = 0 To resultado - 1
                cmbEspecie.Items.Add(oDataSet.Tables("especies").Rows(i).Item(1).ToString())
            Next


        Catch ex As Exception
            MessageBox.Show("No existen datos dentro de esta tabla")
        End Try
    End Sub

    'Recuperamos los ids de habitat y de especie
    Private Sub conseguir_id()
        Dim pConexion As New OleDbConnection
        Dim pDataSet As New DataSet
        Dim busqueda As String

        Dim pDataAdapter = New OleDbDataAdapter("select id_habitat from habitat where nombre_habitat like '" & cmbHabitat.Text & "';", pConexion)
        Dim pCommandBuilder = New OleDbCommandBuilder(pDataAdapter)

        pConexion.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0; Data Source=zoologico.mdb"
        pConexion.Open()
        pDataAdapter.Fill(pDataSet, "habitat")
        busqueda = cmbHabitat.Text



        Try
            If oDataSet.Tables("habitat").Rows.Count > 0 Then
                id_habitat = Int32.Parse(pDataSet.Tables("habitat").Rows(0).Item(0))
            End If
        Catch ex As Exception
            MessageBox.Show("Selecciona un habitat existente")
        End Try

        pConexion.Close()
    End Sub


    Private Sub conseguir_id_especie()

        Dim pConexion As New OleDbConnection
        Dim pDataSet As New DataSet
        Dim busqueda As String

        Dim pDataAdapter = New OleDbDataAdapter("select id_especie from especies where nombre_especie like '" & cmbEspecie.Text & "';", pConexion)
        Dim pCommandBuilder = New OleDbCommandBuilder(pDataAdapter)

        pConexion.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0; Data Source=zoologico.mdb"
        pConexion.Open()
        pDataAdapter.Fill(pDataSet, "especies")
        busqueda = cmbEspecie.Text


        Try
            If oDataSet.Tables("especies").Rows.Count > 0 Then
                id_especie = Int32.Parse(pDataSet.Tables("especies").Rows(0).Item(0))
            End If
        Catch ex As Exception
            MessageBox.Show("Selecciona una especie existente")
        End Try
        pConexion.Close()

    End Sub



    '-------- BTNS GROUP BOX NAVEGACION --------
    Private Sub CambiarBotones(valor1 As Boolean, valor2 As Boolean, valor3 As Boolean, valor4 As Boolean)
        btnSiguiente.Enabled = valor1
        btnAnterior.Enabled = valor2
        btnPrincipio.Enabled = valor3
        btnUltimo.Enabled = valor4
    End Sub

    Private Sub btnSiguiente_Click(sender As Object, e As EventArgs) Handles btnSiguiente.Click
        Posicion += 1
        btnAnterior.Enabled = True

        If oDataSet.Tables("animales").Rows.Count - 1 = Posicion Then CambiarBotones(False, True, True, False)
        Cargar()
    End Sub

    Private Sub btnAnterior_Click(sender As Object, e As EventArgs) Handles btnAnterior.Click
        Posicion -= 1
        btnSiguiente.Enabled = True

        If Posicion = 0 Then CambiarBotones(True, False, False, True)
        Cargar()
    End Sub

    Private Sub btnPrimero_Click(sender As Object, e As EventArgs) Handles btnPrincipio.Click
        Posicion = 0
        btnPrincipio.Enabled = True
        If Posicion = 0 Then CambiarBotones(True, False, False, True)
        Cargar()
    End Sub

    Private Sub btnUltimo_Click(sender As Object, e As EventArgs) Handles btnUltimo.Click
        Posicion = oDataSet.Tables("animales").Rows.Count - 1
        btnUltimo.Enabled = False
        If oDataSet.Tables("animales").Rows.Count - 1 = Posicion Then CambiarBotones(False, True, True, False)
        Cargar()
    End Sub



    Private Sub btnGuardarCambios_Click(sender As Object, e As EventArgs) Handles btnGuardarCambios.Click

        Try
            oDataAdapter.Update(oDataSet, "animales")
            MessageBox.Show("Has guardado con éxito")
            Cargar()
        Catch ex As Exception
            MessageBox.Show("No se ha podido guardar el animal")
        End Try

    End Sub


    Private Sub btnInsertar_Click(sender As Object, e As EventArgs) Handles btnInsertarAnimal.Click
        conseguir_id()
        conseguir_id_especie()
        'MessageBox.Show(id_habitat)
        'MessageBox.Show(id_especie)

        oDataAdapter = Nothing
        oDataAdapter = New OleDbDataAdapter("select * from animales", oConexion)
        oCommandBuilder = New OleDbCommandBuilder(oDataAdapter)
        'llenamos el dataset con la tabla de especie
        'oDataAdapter.Fill(oDataSet, "animales")


        Dim oDataRow As DataRow
        oDataRow = oDataSet.Tables("animales").NewRow()
        oDataRow("nombre_animal") = txtNombreAnimal.Text
        oDataRow("tamanno") = txtTamanno.Text
        oDataRow("peso") = txtPeso.Text
        oDataRow("fk_habitat") = id_habitat
        oDataRow("fk_especie") = id_especie

        oDataSet.Tables("animales").Rows.Add(oDataRow)
        Posicion = 0

        Cargar()
    End Sub


End Class