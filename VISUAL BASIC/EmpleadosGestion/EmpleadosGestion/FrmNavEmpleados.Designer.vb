<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class FrmNavEmpleados
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
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

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.GrupoDatos = New System.Windows.Forms.GroupBox()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.txtSueldo = New System.Windows.Forms.TextBox()
        Me.txtFKzoo = New System.Windows.Forms.TextBox()
        Me.fk_zoo = New System.Windows.Forms.Label()
        Me.btnLimpiarCampos = New System.Windows.Forms.Button()
        Me.txtNivel = New System.Windows.Forms.TextBox()
        Me.txtApellido2 = New System.Windows.Forms.TextBox()
        Me.txtApellido1 = New System.Windows.Forms.TextBox()
        Me.Label6 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.txtNombre = New System.Windows.Forms.TextBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.lblRegistros = New System.Windows.Forms.Label()
        Me.GrupoNavegacion = New System.Windows.Forms.GroupBox()
        Me.btnUltimo = New System.Windows.Forms.Button()
        Me.btnSiguiente = New System.Windows.Forms.Button()
        Me.btnAnterior = New System.Windows.Forms.Button()
        Me.btnPrimero = New System.Windows.Forms.Button()
        Me.GrupoMantenimiento = New System.Windows.Forms.GroupBox()
        Me.btnDeleteAllRows = New System.Windows.Forms.Button()
        Me.btnActualizar = New System.Windows.Forms.Button()
        Me.btnModificar = New System.Windows.Forms.Button()
        Me.btnBorrar = New System.Windows.Forms.Button()
        Me.btnInsertar = New System.Windows.Forms.Button()
        Me.GrupoBusqueda = New System.Windows.Forms.GroupBox()
        Me.btnBuscar = New System.Windows.Forms.Button()
        Me.txtBuscarNivel = New System.Windows.Forms.TextBox()
        Me.lblCodigoPostal = New System.Windows.Forms.Label()
        Me.DataGridDatos = New System.Windows.Forms.DataGridView()
        Me.BackgroundWorker1 = New System.ComponentModel.BackgroundWorker()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.Label7 = New System.Windows.Forms.Label()
        Me.txtCorreo = New System.Windows.Forms.TextBox()
        Me.txtContra = New System.Windows.Forms.TextBox()
        Me.GrupoDatos.SuspendLayout()
        Me.GrupoNavegacion.SuspendLayout()
        Me.GrupoMantenimiento.SuspendLayout()
        Me.GrupoBusqueda.SuspendLayout()
        CType(Me.DataGridDatos, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'GrupoDatos
        '
        Me.GrupoDatos.Controls.Add(Me.txtContra)
        Me.GrupoDatos.Controls.Add(Me.txtCorreo)
        Me.GrupoDatos.Controls.Add(Me.Label7)
        Me.GrupoDatos.Controls.Add(Me.Label5)
        Me.GrupoDatos.Controls.Add(Me.Label4)
        Me.GrupoDatos.Controls.Add(Me.txtSueldo)
        Me.GrupoDatos.Controls.Add(Me.txtFKzoo)
        Me.GrupoDatos.Controls.Add(Me.fk_zoo)
        Me.GrupoDatos.Controls.Add(Me.btnLimpiarCampos)
        Me.GrupoDatos.Controls.Add(Me.txtNivel)
        Me.GrupoDatos.Controls.Add(Me.txtApellido2)
        Me.GrupoDatos.Controls.Add(Me.txtApellido1)
        Me.GrupoDatos.Controls.Add(Me.Label6)
        Me.GrupoDatos.Controls.Add(Me.Label3)
        Me.GrupoDatos.Controls.Add(Me.Label2)
        Me.GrupoDatos.Controls.Add(Me.txtNombre)
        Me.GrupoDatos.Controls.Add(Me.Label1)
        Me.GrupoDatos.Location = New System.Drawing.Point(22, 15)
        Me.GrupoDatos.Margin = New System.Windows.Forms.Padding(2)
        Me.GrupoDatos.Name = "GrupoDatos"
        Me.GrupoDatos.Padding = New System.Windows.Forms.Padding(2)
        Me.GrupoDatos.Size = New System.Drawing.Size(280, 320)
        Me.GrupoDatos.TabIndex = 0
        Me.GrupoDatos.TabStop = False
        Me.GrupoDatos.Text = "Datos Personales"
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Location = New System.Drawing.Point(25, 190)
        Me.Label4.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(40, 13)
        Me.Label4.TabIndex = 16
        Me.Label4.Text = "Sueldo"
        '
        'txtSueldo
        '
        Me.txtSueldo.Location = New System.Drawing.Point(124, 187)
        Me.txtSueldo.Margin = New System.Windows.Forms.Padding(2)
        Me.txtSueldo.Name = "txtSueldo"
        Me.txtSueldo.Size = New System.Drawing.Size(95, 20)
        Me.txtSueldo.TabIndex = 15
        '
        'txtFKzoo
        '
        Me.txtFKzoo.Location = New System.Drawing.Point(124, 253)
        Me.txtFKzoo.Margin = New System.Windows.Forms.Padding(2)
        Me.txtFKzoo.Name = "txtFKzoo"
        Me.txtFKzoo.Size = New System.Drawing.Size(95, 20)
        Me.txtFKzoo.TabIndex = 14
        '
        'fk_zoo
        '
        Me.fk_zoo.AutoSize = True
        Me.fk_zoo.Location = New System.Drawing.Point(36, 256)
        Me.fk_zoo.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.fk_zoo.Name = "fk_zoo"
        Me.fk_zoo.Size = New System.Drawing.Size(39, 13)
        Me.fk_zoo.TabIndex = 13
        Me.fk_zoo.Text = "fk_zoo"
        '
        'btnLimpiarCampos
        '
        Me.btnLimpiarCampos.Location = New System.Drawing.Point(26, 284)
        Me.btnLimpiarCampos.Margin = New System.Windows.Forms.Padding(2)
        Me.btnLimpiarCampos.Name = "btnLimpiarCampos"
        Me.btnLimpiarCampos.Size = New System.Drawing.Size(192, 21)
        Me.btnLimpiarCampos.TabIndex = 12
        Me.btnLimpiarCampos.Text = "Limpiar campos"
        Me.btnLimpiarCampos.UseVisualStyleBackColor = True
        '
        'txtNivel
        '
        Me.txtNivel.Location = New System.Drawing.Point(124, 222)
        Me.txtNivel.Margin = New System.Windows.Forms.Padding(2)
        Me.txtNivel.Name = "txtNivel"
        Me.txtNivel.Size = New System.Drawing.Size(95, 20)
        Me.txtNivel.TabIndex = 11
        '
        'txtApellido2
        '
        Me.txtApellido2.Location = New System.Drawing.Point(122, 95)
        Me.txtApellido2.Margin = New System.Windows.Forms.Padding(2)
        Me.txtApellido2.Name = "txtApellido2"
        Me.txtApellido2.Size = New System.Drawing.Size(95, 20)
        Me.txtApellido2.TabIndex = 8
        '
        'txtApellido1
        '
        Me.txtApellido1.Location = New System.Drawing.Point(122, 62)
        Me.txtApellido1.Margin = New System.Windows.Forms.Padding(2)
        Me.txtApellido1.Name = "txtApellido1"
        Me.txtApellido1.Size = New System.Drawing.Size(95, 20)
        Me.txtApellido1.TabIndex = 7
        '
        'Label6
        '
        Me.Label6.AutoSize = True
        Me.Label6.Location = New System.Drawing.Point(44, 222)
        Me.Label6.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(31, 13)
        Me.Label6.TabIndex = 6
        Me.Label6.Text = "Nivel"
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(23, 95)
        Me.Label3.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(50, 13)
        Me.Label3.TabIndex = 3
        Me.Label3.Text = "Apellido2"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(23, 64)
        Me.Label2.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(50, 13)
        Me.Label2.TabIndex = 2
        Me.Label2.Text = "Apellido1"
        '
        'txtNombre
        '
        Me.txtNombre.Location = New System.Drawing.Point(122, 32)
        Me.txtNombre.Margin = New System.Windows.Forms.Padding(2)
        Me.txtNombre.Name = "txtNombre"
        Me.txtNombre.Size = New System.Drawing.Size(95, 20)
        Me.txtNombre.TabIndex = 1
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(31, 34)
        Me.Label1.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(44, 13)
        Me.Label1.TabIndex = 0
        Me.Label1.Text = "Nombre"
        '
        'lblRegistros
        '
        Me.lblRegistros.AutoSize = True
        Me.lblRegistros.Font = New System.Drawing.Font("Segoe UI", 10.2!)
        Me.lblRegistros.Location = New System.Drawing.Point(35, 337)
        Me.lblRegistros.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.lblRegistros.Name = "lblRegistros"
        Me.lblRegistros.Size = New System.Drawing.Size(85, 19)
        Me.lblRegistros.TabIndex = 1
        Me.lblRegistros.Text = "Nº Registros"
        '
        'GrupoNavegacion
        '
        Me.GrupoNavegacion.Controls.Add(Me.btnUltimo)
        Me.GrupoNavegacion.Controls.Add(Me.btnSiguiente)
        Me.GrupoNavegacion.Controls.Add(Me.btnAnterior)
        Me.GrupoNavegacion.Controls.Add(Me.btnPrimero)
        Me.GrupoNavegacion.Location = New System.Drawing.Point(326, 24)
        Me.GrupoNavegacion.Margin = New System.Windows.Forms.Padding(2)
        Me.GrupoNavegacion.Name = "GrupoNavegacion"
        Me.GrupoNavegacion.Padding = New System.Windows.Forms.Padding(2)
        Me.GrupoNavegacion.Size = New System.Drawing.Size(278, 61)
        Me.GrupoNavegacion.TabIndex = 2
        Me.GrupoNavegacion.TabStop = False
        Me.GrupoNavegacion.Text = "Navegación"
        '
        'btnUltimo
        '
        Me.btnUltimo.Location = New System.Drawing.Point(190, 31)
        Me.btnUltimo.Margin = New System.Windows.Forms.Padding(2)
        Me.btnUltimo.Name = "btnUltimo"
        Me.btnUltimo.Size = New System.Drawing.Size(40, 18)
        Me.btnUltimo.TabIndex = 3
        Me.btnUltimo.Text = ">>"
        Me.btnUltimo.UseVisualStyleBackColor = True
        '
        'btnSiguiente
        '
        Me.btnSiguiente.Location = New System.Drawing.Point(139, 31)
        Me.btnSiguiente.Margin = New System.Windows.Forms.Padding(2)
        Me.btnSiguiente.Name = "btnSiguiente"
        Me.btnSiguiente.Size = New System.Drawing.Size(40, 18)
        Me.btnSiguiente.TabIndex = 2
        Me.btnSiguiente.Text = ">"
        Me.btnSiguiente.UseVisualStyleBackColor = True
        '
        'btnAnterior
        '
        Me.btnAnterior.Location = New System.Drawing.Point(86, 31)
        Me.btnAnterior.Margin = New System.Windows.Forms.Padding(2)
        Me.btnAnterior.Name = "btnAnterior"
        Me.btnAnterior.Size = New System.Drawing.Size(40, 18)
        Me.btnAnterior.TabIndex = 1
        Me.btnAnterior.Text = "<"
        Me.btnAnterior.UseVisualStyleBackColor = True
        '
        'btnPrimero
        '
        Me.btnPrimero.Location = New System.Drawing.Point(32, 31)
        Me.btnPrimero.Margin = New System.Windows.Forms.Padding(2)
        Me.btnPrimero.Name = "btnPrimero"
        Me.btnPrimero.Size = New System.Drawing.Size(40, 18)
        Me.btnPrimero.TabIndex = 0
        Me.btnPrimero.Text = "<<"
        Me.btnPrimero.UseVisualStyleBackColor = True
        '
        'GrupoMantenimiento
        '
        Me.GrupoMantenimiento.Controls.Add(Me.btnDeleteAllRows)
        Me.GrupoMantenimiento.Controls.Add(Me.btnActualizar)
        Me.GrupoMantenimiento.Controls.Add(Me.btnModificar)
        Me.GrupoMantenimiento.Controls.Add(Me.btnBorrar)
        Me.GrupoMantenimiento.Controls.Add(Me.btnInsertar)
        Me.GrupoMantenimiento.Location = New System.Drawing.Point(316, 110)
        Me.GrupoMantenimiento.Margin = New System.Windows.Forms.Padding(2)
        Me.GrupoMantenimiento.Name = "GrupoMantenimiento"
        Me.GrupoMantenimiento.Padding = New System.Windows.Forms.Padding(2)
        Me.GrupoMantenimiento.Size = New System.Drawing.Size(296, 79)
        Me.GrupoMantenimiento.TabIndex = 3
        Me.GrupoMantenimiento.TabStop = False
        Me.GrupoMantenimiento.Text = "Mantenimiento"
        '
        'btnDeleteAllRows
        '
        Me.btnDeleteAllRows.Location = New System.Drawing.Point(62, 51)
        Me.btnDeleteAllRows.Margin = New System.Windows.Forms.Padding(2)
        Me.btnDeleteAllRows.Name = "btnDeleteAllRows"
        Me.btnDeleteAllRows.Size = New System.Drawing.Size(168, 22)
        Me.btnDeleteAllRows.TabIndex = 4
        Me.btnDeleteAllRows.Text = "Eliminar todas las filas"
        Me.btnDeleteAllRows.UseVisualStyleBackColor = True
        '
        'btnActualizar
        '
        Me.btnActualizar.Location = New System.Drawing.Point(148, 25)
        Me.btnActualizar.Margin = New System.Windows.Forms.Padding(2)
        Me.btnActualizar.Name = "btnActualizar"
        Me.btnActualizar.Size = New System.Drawing.Size(70, 22)
        Me.btnActualizar.TabIndex = 3
        Me.btnActualizar.Text = "Actualizar"
        Me.btnActualizar.UseVisualStyleBackColor = True
        '
        'btnModificar
        '
        Me.btnModificar.Location = New System.Drawing.Point(78, 25)
        Me.btnModificar.Margin = New System.Windows.Forms.Padding(2)
        Me.btnModificar.Name = "btnModificar"
        Me.btnModificar.Size = New System.Drawing.Size(65, 22)
        Me.btnModificar.TabIndex = 2
        Me.btnModificar.Text = "Modificar"
        Me.btnModificar.UseVisualStyleBackColor = True
        '
        'btnBorrar
        '
        Me.btnBorrar.Location = New System.Drawing.Point(223, 25)
        Me.btnBorrar.Margin = New System.Windows.Forms.Padding(2)
        Me.btnBorrar.Name = "btnBorrar"
        Me.btnBorrar.Size = New System.Drawing.Size(58, 22)
        Me.btnBorrar.TabIndex = 1
        Me.btnBorrar.Text = "Borrar"
        Me.btnBorrar.UseVisualStyleBackColor = True
        '
        'btnInsertar
        '
        Me.btnInsertar.Location = New System.Drawing.Point(16, 25)
        Me.btnInsertar.Margin = New System.Windows.Forms.Padding(2)
        Me.btnInsertar.Name = "btnInsertar"
        Me.btnInsertar.Size = New System.Drawing.Size(58, 22)
        Me.btnInsertar.TabIndex = 0
        Me.btnInsertar.Text = "Insertar"
        Me.btnInsertar.UseVisualStyleBackColor = True
        '
        'GrupoBusqueda
        '
        Me.GrupoBusqueda.Controls.Add(Me.btnBuscar)
        Me.GrupoBusqueda.Controls.Add(Me.txtBuscarNivel)
        Me.GrupoBusqueda.Controls.Add(Me.lblCodigoPostal)
        Me.GrupoBusqueda.Location = New System.Drawing.Point(316, 220)
        Me.GrupoBusqueda.Margin = New System.Windows.Forms.Padding(2)
        Me.GrupoBusqueda.Name = "GrupoBusqueda"
        Me.GrupoBusqueda.Padding = New System.Windows.Forms.Padding(2)
        Me.GrupoBusqueda.Size = New System.Drawing.Size(296, 58)
        Me.GrupoBusqueda.TabIndex = 4
        Me.GrupoBusqueda.TabStop = False
        Me.GrupoBusqueda.Text = "Búsqueda"
        '
        'btnBuscar
        '
        Me.btnBuscar.Location = New System.Drawing.Point(185, 27)
        Me.btnBuscar.Margin = New System.Windows.Forms.Padding(2)
        Me.btnBuscar.Name = "btnBuscar"
        Me.btnBuscar.Size = New System.Drawing.Size(70, 19)
        Me.btnBuscar.TabIndex = 2
        Me.btnBuscar.Text = "Buscar"
        Me.btnBuscar.UseVisualStyleBackColor = True
        '
        'txtBuscarNivel
        '
        Me.txtBuscarNivel.Location = New System.Drawing.Point(62, 27)
        Me.txtBuscarNivel.Margin = New System.Windows.Forms.Padding(2)
        Me.txtBuscarNivel.Name = "txtBuscarNivel"
        Me.txtBuscarNivel.Size = New System.Drawing.Size(95, 20)
        Me.txtBuscarNivel.TabIndex = 1
        '
        'lblCodigoPostal
        '
        Me.lblCodigoPostal.AutoSize = True
        Me.lblCodigoPostal.Location = New System.Drawing.Point(24, 30)
        Me.lblCodigoPostal.Margin = New System.Windows.Forms.Padding(2, 0, 2, 0)
        Me.lblCodigoPostal.Name = "lblCodigoPostal"
        Me.lblCodigoPostal.Size = New System.Drawing.Size(16, 13)
        Me.lblCodigoPostal.TabIndex = 0
        Me.lblCodigoPostal.Text = "Id"
        '
        'DataGridDatos
        '
        Me.DataGridDatos.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.DataGridDatos.Location = New System.Drawing.Point(67, 361)
        Me.DataGridDatos.Margin = New System.Windows.Forms.Padding(2)
        Me.DataGridDatos.Name = "DataGridDatos"
        Me.DataGridDatos.RowHeadersWidth = 51
        Me.DataGridDatos.RowTemplate.Height = 29
        Me.DataGridDatos.Size = New System.Drawing.Size(508, 93)
        Me.DataGridDatos.TabIndex = 5
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Location = New System.Drawing.Point(26, 129)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(38, 13)
        Me.Label5.TabIndex = 17
        Me.Label5.Text = "Correo"
        '
        'Label7
        '
        Me.Label7.AutoSize = True
        Me.Label7.Location = New System.Drawing.Point(14, 161)
        Me.Label7.Name = "Label7"
        Me.Label7.Size = New System.Drawing.Size(61, 13)
        Me.Label7.TabIndex = 18
        Me.Label7.Text = "Contraseña"
        '
        'txtCorreo
        '
        Me.txtCorreo.Location = New System.Drawing.Point(122, 129)
        Me.txtCorreo.Name = "txtCorreo"
        Me.txtCorreo.Size = New System.Drawing.Size(100, 20)
        Me.txtCorreo.TabIndex = 19
        '
        'txtContra
        '
        Me.txtContra.Location = New System.Drawing.Point(122, 158)
        Me.txtContra.Name = "txtContra"
        Me.txtContra.Size = New System.Drawing.Size(100, 20)
        Me.txtContra.TabIndex = 20
        '
        'FrmNavEmpleados
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(632, 465)
        Me.Controls.Add(Me.DataGridDatos)
        Me.Controls.Add(Me.GrupoBusqueda)
        Me.Controls.Add(Me.GrupoMantenimiento)
        Me.Controls.Add(Me.GrupoNavegacion)
        Me.Controls.Add(Me.lblRegistros)
        Me.Controls.Add(Me.GrupoDatos)
        Me.Margin = New System.Windows.Forms.Padding(2)
        Me.Name = "FrmNavEmpleados"
        Me.Text = "Form1"
        Me.GrupoDatos.ResumeLayout(False)
        Me.GrupoDatos.PerformLayout()
        Me.GrupoNavegacion.ResumeLayout(False)
        Me.GrupoMantenimiento.ResumeLayout(False)
        Me.GrupoBusqueda.ResumeLayout(False)
        Me.GrupoBusqueda.PerformLayout()
        CType(Me.DataGridDatos, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents GrupoDatos As GroupBox
    Friend WithEvents Label1 As Label
    Friend WithEvents Label3 As Label
    Friend WithEvents Label2 As Label
    Friend WithEvents txtNombre As TextBox
    Friend WithEvents txtNivel As TextBox
    Friend WithEvents txtApellido2 As TextBox
    Friend WithEvents txtApellido1 As TextBox
    Friend WithEvents Label6 As Label
    Friend WithEvents lblRegistros As Label
    Friend WithEvents GrupoNavegacion As GroupBox
    Friend WithEvents btnPrimero As Button
    Friend WithEvents btnUltimo As Button
    Friend WithEvents btnSiguiente As Button
    Friend WithEvents btnAnterior As Button
    Friend WithEvents GrupoMantenimiento As GroupBox
    Friend WithEvents btnInsertar As Button
    Friend WithEvents btnBorrar As Button
    Friend WithEvents btnActualizar As Button
    Friend WithEvents btnModificar As Button
    Friend WithEvents btnDeleteAllRows As Button
    Friend WithEvents btnLimpiarCampos As Button
    Friend WithEvents GrupoBusqueda As GroupBox
    Friend WithEvents lblCodigoPostal As Label
    Friend WithEvents txtBuscarNivel As TextBox
    Friend WithEvents btnBuscar As Button
    Friend WithEvents DataGridDatos As DataGridView
    Friend WithEvents fk_zoo As Label
    Friend WithEvents txtFKzoo As TextBox
    Friend WithEvents txtSueldo As TextBox
    Friend WithEvents Label4 As Label
    Friend WithEvents BackgroundWorker1 As System.ComponentModel.BackgroundWorker
    Friend WithEvents txtContra As TextBox
    Friend WithEvents txtCorreo As TextBox
    Friend WithEvents Label7 As Label
    Friend WithEvents Label5 As Label
End Class
