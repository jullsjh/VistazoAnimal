Module Module1
    Public nivel As String
    Public id_usuario As Integer
    Public nombre_usuario As String

    Public InsertarFrm As New FrmAnadirAnimal
    Public ConsultasFrm As New FrmConsultas
    Public NavEmpleadosBBDFrm As New FrmNavEmpleados
    Public loginFrm As New Login
    Public InicioFrm As New FrmInicio
    Sub main()
        ' NaveBBDDFrm = New FrmNaveBBDD
        Application.Run(loginFrm)
    End Sub


    'properties par cambiar de color al modo oscuro
    Public m_FormBackgroundColor As Color
    Public m_FormTextColor As Color


    Public Property FormTextColor As Color
        Get
            Return m_FormTextColor
        End Get
        Set(value As Color)
            m_FormTextColor = value
            'For Each Frm As Form In Application.OpenForms
            '    Frm.ForeColor = m_FormTextColor
            'Next
        End Set
    End Property


    Public Property FormBackgroundColor As Color
        Get
            Return m_FormBackgroundColor
        End Get
        Set(value As Color)
            m_FormBackgroundColor = value
            'For Each Frm As Form In Application.OpenForms
            '    Frm.BackColor = m_FormBackgroundColor
            'Next
        End Set
    End Property


End Module
