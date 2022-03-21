
Public Class FrmInicio
    Inherits System.Windows.Forms.Form


    Dim _nivel As String
    Dim id As Integer

    'Prueba de que hemos 
    Private Sub FrmInicio_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        MessageBox.Show("Bienvenido: " & Module1.nombre_usuario)
        'MessageBox.Show(Module1.m_FormBackgroundColor.ToString())
    End Sub


    Private Sub EmpleadosToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles EmpleadosToolStripMenuItem.Click
        Datos()

    End Sub

    Private Sub GenerarConsultaToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles GenerarConsultaToolStripMenuItem.Click
        Consultas()
    End Sub

    Private Sub InsertarNuevoAnimalToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles InsertarNuevoAnimalToolStripMenuItem.Click
        Insertar()
    End Sub


    'Metodos que nos abren las dos ventanas
    Public Sub Datos()
        NavEmpleadosBBDFrm = New FrmNavEmpleados
        NavEmpleadosBBDFrm.MdiParent = InicioFrm
        NavEmpleadosBBDFrm.Show()
        'BtnBBDD.Enabled = False
    End Sub
    Public Sub Consultas()
        ConsultasFrm = New FrmConsultas
        ConsultasFrm.MdiParent = InicioFrm
        ConsultasFrm.Show()
        'BtnGenerarConsulta.Enabled = False
    End Sub
    Public Sub Insertar()
        InsertarFrm = New FrmAnadirAnimal
        InsertarFrm.MdiParent = InicioFrm
        InsertarFrm.Show()
    End Sub

    Private Sub SalirToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles SalirToolStripMenuItem.Click
        Me.Hide()
        loginFrm.txtCorreo.Text = ""
        loginFrm.txtContra.Text = ""
        loginFrm.Show()
    End Sub
End Class