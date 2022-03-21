<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class FrmInicio
    Inherits System.Windows.Forms.Form

    'Form reemplaza a Dispose para limpiar la lista de componentes.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Requerido por el Diseñador de Windows Forms
    Private components As System.ComponentModel.IContainer

    'NOTA: el Diseñador de Windows Forms necesita el siguiente procedimiento
    'Se puede modificar usando el Diseñador de Windows Forms.  
    'No lo modifique con el editor de código.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.MenuStrip1 = New System.Windows.Forms.MenuStrip()
        Me.MnuBBDD = New System.Windows.Forms.ToolStripMenuItem()
        Me.MnuBaseDeDatos = New System.Windows.Forms.ToolStripMenuItem()
        Me.EmpleadosToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.GenerarConsultaToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.InsertarNuevoAnimalToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.SalirToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.MenuStrip1.SuspendLayout()
        Me.SuspendLayout()
        '
        'MenuStrip1
        '
        Me.MenuStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.MnuBBDD, Me.SalirToolStripMenuItem})
        Me.MenuStrip1.Location = New System.Drawing.Point(0, 0)
        Me.MenuStrip1.Name = "MenuStrip1"
        Me.MenuStrip1.Size = New System.Drawing.Size(800, 24)
        Me.MenuStrip1.TabIndex = 0
        Me.MenuStrip1.Text = "MenuStrip1"
        '
        'MnuBBDD
        '
        Me.MnuBBDD.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.MnuBaseDeDatos, Me.GenerarConsultaToolStripMenuItem, Me.InsertarNuevoAnimalToolStripMenuItem})
        Me.MnuBBDD.Name = "MnuBBDD"
        Me.MnuBBDD.Size = New System.Drawing.Size(49, 20)
        Me.MnuBBDD.Text = "BBDD"
        '
        'MnuBaseDeDatos
        '
        Me.MnuBaseDeDatos.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.EmpleadosToolStripMenuItem})
        Me.MnuBaseDeDatos.Name = "MnuBaseDeDatos"
        Me.MnuBaseDeDatos.Size = New System.Drawing.Size(188, 22)
        Me.MnuBaseDeDatos.Text = "Base de datos"
        '
        'EmpleadosToolStripMenuItem
        '
        Me.EmpleadosToolStripMenuItem.Name = "EmpleadosToolStripMenuItem"
        Me.EmpleadosToolStripMenuItem.Size = New System.Drawing.Size(132, 22)
        Me.EmpleadosToolStripMenuItem.Text = "Empleados"
        '
        'GenerarConsultaToolStripMenuItem
        '
        Me.GenerarConsultaToolStripMenuItem.Name = "GenerarConsultaToolStripMenuItem"
        Me.GenerarConsultaToolStripMenuItem.Size = New System.Drawing.Size(188, 22)
        Me.GenerarConsultaToolStripMenuItem.Text = "Generar Consulta"
        '
        'InsertarNuevoAnimalToolStripMenuItem
        '
        Me.InsertarNuevoAnimalToolStripMenuItem.Name = "InsertarNuevoAnimalToolStripMenuItem"
        Me.InsertarNuevoAnimalToolStripMenuItem.Size = New System.Drawing.Size(188, 22)
        Me.InsertarNuevoAnimalToolStripMenuItem.Text = "Insertar nuevo animal"
        '
        'SalirToolStripMenuItem
        '
        Me.SalirToolStripMenuItem.Name = "SalirToolStripMenuItem"
        Me.SalirToolStripMenuItem.Size = New System.Drawing.Size(41, 20)
        Me.SalirToolStripMenuItem.Text = "Salir"
        '
        'FrmInicio
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(800, 507)
        Me.Controls.Add(Me.MenuStrip1)
        Me.IsMdiContainer = True
        Me.MainMenuStrip = Me.MenuStrip1
        Me.Name = "FrmInicio"
        Me.Text = "FrnInicio"
        Me.MenuStrip1.ResumeLayout(False)
        Me.MenuStrip1.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents MenuStrip1 As MenuStrip
    Friend WithEvents MnuBBDD As ToolStripMenuItem
    Friend WithEvents MnuBaseDeDatos As ToolStripMenuItem
    Friend WithEvents EmpleadosToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents GenerarConsultaToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents SalirToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents InsertarNuevoAnimalToolStripMenuItem As ToolStripMenuItem
End Class
