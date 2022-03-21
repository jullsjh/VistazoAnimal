<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class FrmAnadirAnimal
    Inherits System.Windows.Forms.Form

    'Form reemplaza a Dispose para limpiar la lista de componentes.
    <System.Diagnostics.DebuggerNonUserCode()>
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
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Me.txtNombreAnimal = New System.Windows.Forms.TextBox()
        Me.GroupBox1 = New System.Windows.Forms.GroupBox()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.cmbEspecie = New System.Windows.Forms.ComboBox()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.cmbHabitat = New System.Windows.Forms.ComboBox()
        Me.txtPeso = New System.Windows.Forms.TextBox()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.txtTamanno = New System.Windows.Forms.TextBox()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.ContextMenuStrip1 = New System.Windows.Forms.ContextMenuStrip(Me.components)
        Me.btnGuardarCambios = New System.Windows.Forms.Button()
        Me.btnInsertarAnimal = New System.Windows.Forms.Button()
        Me.btnSiguiente = New System.Windows.Forms.Button()
        Me.btnAnterior = New System.Windows.Forms.Button()
        Me.btnUltimo = New System.Windows.Forms.Button()
        Me.btnPrincipio = New System.Windows.Forms.Button()
        Me.lblRegistros = New System.Windows.Forms.Label()
        Me.GroupBox1.SuspendLayout()
        Me.SuspendLayout()
        '
        'txtNombreAnimal
        '
        Me.txtNombreAnimal.Location = New System.Drawing.Point(132, 31)
        Me.txtNombreAnimal.Name = "txtNombreAnimal"
        Me.txtNombreAnimal.Size = New System.Drawing.Size(155, 20)
        Me.txtNombreAnimal.TabIndex = 0
        '
        'GroupBox1
        '
        Me.GroupBox1.Controls.Add(Me.Label5)
        Me.GroupBox1.Controls.Add(Me.cmbEspecie)
        Me.GroupBox1.Controls.Add(Me.Label4)
        Me.GroupBox1.Controls.Add(Me.cmbHabitat)
        Me.GroupBox1.Controls.Add(Me.txtPeso)
        Me.GroupBox1.Controls.Add(Me.Label3)
        Me.GroupBox1.Controls.Add(Me.txtTamanno)
        Me.GroupBox1.Controls.Add(Me.Label2)
        Me.GroupBox1.Controls.Add(Me.Label1)
        Me.GroupBox1.Controls.Add(Me.txtNombreAnimal)
        Me.GroupBox1.Location = New System.Drawing.Point(27, 52)
        Me.GroupBox1.Name = "GroupBox1"
        Me.GroupBox1.Size = New System.Drawing.Size(754, 182)
        Me.GroupBox1.TabIndex = 1
        Me.GroupBox1.TabStop = False
        Me.GroupBox1.Text = "Insertar animal"
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Location = New System.Drawing.Point(454, 117)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(45, 13)
        Me.Label5.TabIndex = 9
        Me.Label5.Text = "Especie"
        '
        'cmbEspecie
        '
        Me.cmbEspecie.FormattingEnabled = True
        Me.cmbEspecie.Location = New System.Drawing.Point(547, 109)
        Me.cmbEspecie.Name = "cmbEspecie"
        Me.cmbEspecie.Size = New System.Drawing.Size(148, 21)
        Me.cmbEspecie.TabIndex = 8
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Location = New System.Drawing.Point(458, 51)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(41, 13)
        Me.Label4.TabIndex = 7
        Me.Label4.Text = "Habitat"
        '
        'cmbHabitat
        '
        Me.cmbHabitat.FormattingEnabled = True
        Me.cmbHabitat.Location = New System.Drawing.Point(547, 48)
        Me.cmbHabitat.Name = "cmbHabitat"
        Me.cmbHabitat.Size = New System.Drawing.Size(148, 21)
        Me.cmbHabitat.TabIndex = 6
        '
        'txtPeso
        '
        Me.txtPeso.Location = New System.Drawing.Point(132, 126)
        Me.txtPeso.Name = "txtPeso"
        Me.txtPeso.Size = New System.Drawing.Size(155, 20)
        Me.txtPeso.TabIndex = 5
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(19, 133)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(31, 13)
        Me.Label3.TabIndex = 4
        Me.Label3.Text = "Peso"
        '
        'txtTamanno
        '
        Me.txtTamanno.Location = New System.Drawing.Point(132, 81)
        Me.txtTamanno.Name = "txtTamanno"
        Me.txtTamanno.Size = New System.Drawing.Size(155, 20)
        Me.txtTamanno.TabIndex = 3
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(19, 81)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(69, 13)
        Me.Label2.TabIndex = 2
        Me.Label2.Text = "Tamaño (cm)"
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(19, 34)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(94, 13)
        Me.Label1.TabIndex = 1
        Me.Label1.Text = "Nombre del animal"
        '
        'ContextMenuStrip1
        '
        Me.ContextMenuStrip1.Name = "ContextMenuStrip1"
        Me.ContextMenuStrip1.Size = New System.Drawing.Size(61, 4)
        '
        'btnGuardarCambios
        '
        Me.btnGuardarCambios.Location = New System.Drawing.Point(422, 390)
        Me.btnGuardarCambios.Name = "btnGuardarCambios"
        Me.btnGuardarCambios.Size = New System.Drawing.Size(176, 38)
        Me.btnGuardarCambios.TabIndex = 3
        Me.btnGuardarCambios.Text = "Guardar Cambios"
        Me.btnGuardarCambios.UseVisualStyleBackColor = True
        '
        'btnInsertarAnimal
        '
        Me.btnInsertarAnimal.Location = New System.Drawing.Point(223, 390)
        Me.btnInsertarAnimal.Name = "btnInsertarAnimal"
        Me.btnInsertarAnimal.Size = New System.Drawing.Size(176, 38)
        Me.btnInsertarAnimal.TabIndex = 4
        Me.btnInsertarAnimal.Text = "Insertar Animal"
        Me.btnInsertarAnimal.UseVisualStyleBackColor = True
        '
        'btnSiguiente
        '
        Me.btnSiguiente.Location = New System.Drawing.Point(433, 299)
        Me.btnSiguiente.Name = "btnSiguiente"
        Me.btnSiguiente.Size = New System.Drawing.Size(71, 27)
        Me.btnSiguiente.TabIndex = 6
        Me.btnSiguiente.Text = ">"
        Me.btnSiguiente.UseVisualStyleBackColor = True
        '
        'btnAnterior
        '
        Me.btnAnterior.Location = New System.Drawing.Point(328, 299)
        Me.btnAnterior.Name = "btnAnterior"
        Me.btnAnterior.Size = New System.Drawing.Size(71, 27)
        Me.btnAnterior.TabIndex = 7
        Me.btnAnterior.Text = "<"
        Me.btnAnterior.UseVisualStyleBackColor = True
        '
        'btnUltimo
        '
        Me.btnUltimo.Location = New System.Drawing.Point(527, 299)
        Me.btnUltimo.Name = "btnUltimo"
        Me.btnUltimo.Size = New System.Drawing.Size(71, 27)
        Me.btnUltimo.TabIndex = 8
        Me.btnUltimo.Text = ">>"
        Me.btnUltimo.UseVisualStyleBackColor = True
        '
        'btnPrincipio
        '
        Me.btnPrincipio.Location = New System.Drawing.Point(228, 299)
        Me.btnPrincipio.Name = "btnPrincipio"
        Me.btnPrincipio.Size = New System.Drawing.Size(71, 27)
        Me.btnPrincipio.TabIndex = 9
        Me.btnPrincipio.Text = "<<"
        Me.btnPrincipio.UseVisualStyleBackColor = True
        '
        'lblRegistros
        '
        Me.lblRegistros.AutoSize = True
        Me.lblRegistros.Location = New System.Drawing.Point(387, 257)
        Me.lblRegistros.Name = "lblRegistros"
        Me.lblRegistros.Size = New System.Drawing.Size(51, 13)
        Me.lblRegistros.TabIndex = 10
        Me.lblRegistros.Text = "Registros"
        '
        'FrmAnadirAnimal
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(821, 494)
        Me.Controls.Add(Me.lblRegistros)
        Me.Controls.Add(Me.btnPrincipio)
        Me.Controls.Add(Me.btnUltimo)
        Me.Controls.Add(Me.btnAnterior)
        Me.Controls.Add(Me.btnSiguiente)
        Me.Controls.Add(Me.btnInsertarAnimal)
        Me.Controls.Add(Me.btnGuardarCambios)
        Me.Controls.Add(Me.GroupBox1)
        Me.Name = "FrmAnadirAnimal"
        Me.Text = "AnadirAnimal"
        Me.GroupBox1.ResumeLayout(False)
        Me.GroupBox1.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents txtNombreAnimal As TextBox
    Friend WithEvents GroupBox1 As GroupBox
    Friend WithEvents ContextMenuStrip1 As ContextMenuStrip
    Friend WithEvents Label1 As Label
    Friend WithEvents Label5 As Label
    Friend WithEvents cmbEspecie As ComboBox
    Friend WithEvents Label4 As Label
    Friend WithEvents cmbHabitat As ComboBox
    Friend WithEvents txtPeso As TextBox
    Friend WithEvents Label3 As Label
    Friend WithEvents txtTamanno As TextBox
    Friend WithEvents Label2 As Label
    Friend WithEvents btnGuardarCambios As Button
    Friend WithEvents btnInsertarAnimal As Button
    Friend WithEvents btnSiguiente As Button
    Friend WithEvents btnAnterior As Button
    Friend WithEvents btnUltimo As Button
    Friend WithEvents btnPrincipio As Button
    Friend WithEvents lblRegistros As Label
End Class
