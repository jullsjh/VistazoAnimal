<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class FrmConsultas
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
        Me.LblNoDatos = New System.Windows.Forms.Label()
        Me.BtnAceptar = New System.Windows.Forms.Button()
        Me.DtgDatos = New System.Windows.Forms.DataGrid()
        Me.LblDatoBuscar = New System.Windows.Forms.Label()
        Me.LblSelect = New System.Windows.Forms.Label()
        Me.TxtSelect = New System.Windows.Forms.TextBox()
        Me.TxtDatoBuscar = New System.Windows.Forms.TextBox()
        Me.OptMenor = New System.Windows.Forms.RadioButton()
        Me.OptMayor = New System.Windows.Forms.RadioButton()
        Me.OptIgual = New System.Windows.Forms.RadioButton()
        Me.CmbCampos = New System.Windows.Forms.ComboBox()
        Me.CmbTablas = New System.Windows.Forms.ComboBox()
        CType(Me.DtgDatos, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'LblNoDatos
        '
        Me.LblNoDatos.BackColor = System.Drawing.SystemColors.AppWorkspace
        Me.LblNoDatos.Font = New System.Drawing.Font("Microsoft Sans Serif", 21.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.LblNoDatos.Location = New System.Drawing.Point(251, 272)
        Me.LblNoDatos.Name = "LblNoDatos"
        Me.LblNoDatos.Size = New System.Drawing.Size(307, 37)
        Me.LblNoDatos.TabIndex = 23
        Me.LblNoDatos.Text = "No Existen Datos"
        Me.LblNoDatos.Visible = False
        '
        'BtnAceptar
        '
        Me.BtnAceptar.Enabled = False
        Me.BtnAceptar.Location = New System.Drawing.Point(587, 87)
        Me.BtnAceptar.Name = "BtnAceptar"
        Me.BtnAceptar.Size = New System.Drawing.Size(125, 28)
        Me.BtnAceptar.TabIndex = 22
        Me.BtnAceptar.Text = "Aceptar"
        '
        'DtgDatos
        '
        Me.DtgDatos.DataMember = ""
        Me.DtgDatos.HeaderForeColor = System.Drawing.SystemColors.ControlText
        Me.DtgDatos.Location = New System.Drawing.Point(59, 179)
        Me.DtgDatos.Name = "DtgDatos"
        Me.DtgDatos.Size = New System.Drawing.Size(701, 250)
        Me.DtgDatos.TabIndex = 21
        '
        'LblDatoBuscar
        '
        Me.LblDatoBuscar.Enabled = False
        Me.LblDatoBuscar.Location = New System.Drawing.Point(548, 22)
        Me.LblDatoBuscar.Name = "LblDatoBuscar"
        Me.LblDatoBuscar.Size = New System.Drawing.Size(106, 27)
        Me.LblDatoBuscar.TabIndex = 20
        Me.LblDatoBuscar.Text = "Dato a Buscar:"
        '
        'LblSelect
        '
        Me.LblSelect.Location = New System.Drawing.Point(59, 96)
        Me.LblSelect.Name = "LblSelect"
        Me.LblSelect.Size = New System.Drawing.Size(67, 27)
        Me.LblSelect.TabIndex = 19
        Me.LblSelect.Text = "Consulta:"
        '
        'TxtSelect
        '
        Me.TxtSelect.Location = New System.Drawing.Point(59, 133)
        Me.TxtSelect.Name = "TxtSelect"
        Me.TxtSelect.Size = New System.Drawing.Size(691, 22)
        Me.TxtSelect.TabIndex = 18
        '
        'TxtDatoBuscar
        '
        Me.TxtDatoBuscar.Enabled = False
        Me.TxtDatoBuscar.Location = New System.Drawing.Point(548, 59)
        Me.TxtDatoBuscar.Name = "TxtDatoBuscar"
        Me.TxtDatoBuscar.Size = New System.Drawing.Size(202, 22)
        Me.TxtDatoBuscar.TabIndex = 17
        '
        'OptMenor
        '
        Me.OptMenor.Enabled = False
        Me.OptMenor.Location = New System.Drawing.Point(462, 96)
        Me.OptMenor.Name = "OptMenor"
        Me.OptMenor.Size = New System.Drawing.Size(48, 28)
        Me.OptMenor.TabIndex = 16
        Me.OptMenor.Text = "<"
        '
        'OptMayor
        '
        Me.OptMayor.Enabled = False
        Me.OptMayor.Location = New System.Drawing.Point(462, 59)
        Me.OptMayor.Name = "OptMayor"
        Me.OptMayor.Size = New System.Drawing.Size(48, 28)
        Me.OptMayor.TabIndex = 15
        Me.OptMayor.Text = ">"
        '
        'OptIgual
        '
        Me.OptIgual.Enabled = False
        Me.OptIgual.Location = New System.Drawing.Point(462, 22)
        Me.OptIgual.Name = "OptIgual"
        Me.OptIgual.Size = New System.Drawing.Size(48, 28)
        Me.OptIgual.TabIndex = 14
        Me.OptIgual.Text = "="
        '
        'CmbCampos
        '
        Me.CmbCampos.Location = New System.Drawing.Point(232, 22)
        Me.CmbCampos.Name = "CmbCampos"
        Me.CmbCampos.Size = New System.Drawing.Size(182, 24)
        Me.CmbCampos.TabIndex = 13
        Me.CmbCampos.Text = "Seleccione un Campo"
        '
        'CmbTablas
        '
        Me.CmbTablas.Location = New System.Drawing.Point(40, 22)
        Me.CmbTablas.Name = "CmbTablas"
        Me.CmbTablas.Size = New System.Drawing.Size(163, 24)
        Me.CmbTablas.TabIndex = 12
        Me.CmbTablas.Text = "Seleccione una tabla"
        '
        'FrmConsultas
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(8.0!, 16.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(800, 450)
        Me.Controls.Add(Me.LblNoDatos)
        Me.Controls.Add(Me.BtnAceptar)
        Me.Controls.Add(Me.DtgDatos)
        Me.Controls.Add(Me.LblDatoBuscar)
        Me.Controls.Add(Me.LblSelect)
        Me.Controls.Add(Me.TxtSelect)
        Me.Controls.Add(Me.TxtDatoBuscar)
        Me.Controls.Add(Me.OptMenor)
        Me.Controls.Add(Me.OptMayor)
        Me.Controls.Add(Me.OptIgual)
        Me.Controls.Add(Me.CmbCampos)
        Me.Controls.Add(Me.CmbTablas)
        Me.Name = "FrmConsultas"
        Me.Text = "Form2"
        CType(Me.DtgDatos, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents LblNoDatos As Label
    Friend WithEvents BtnAceptar As Button
    Friend WithEvents DtgDatos As DataGrid
    Friend WithEvents LblDatoBuscar As Label
    Friend WithEvents LblSelect As Label
    Friend WithEvents TxtSelect As TextBox
    Friend WithEvents TxtDatoBuscar As TextBox
    Friend WithEvents OptMenor As RadioButton
    Friend WithEvents OptMayor As RadioButton
    Friend WithEvents OptIgual As RadioButton
    Friend WithEvents CmbCampos As ComboBox
    Friend WithEvents CmbTablas As ComboBox
End Class
