; Script Inno Setup pour Système Expert - Droit du Numérique
; Nécessite Inno Setup 6.0 ou supérieur
; Télécharger : https://jrsoftware.org/isdl.php

#define MyAppName "Système Expert - Droit du Numérique"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Système Expert Académique"
#define MyAppURL "https://github.com/votre-repo"
#define MyAppExeName "SystemeExpertDroitNumerique.exe"

[Setup]
; Informations de l'application
AppId={{12345678-1234-1234-1234-123456789ABC}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}

; Répertoire d'installation par défaut
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}

; Fichier de sortie
OutputDir=output
OutputBaseFilename=SystemeExpertDroitNumerique_Setup_v{#MyAppVersion}

; Icône de l'installateur
SetupIconFile=icon.ico

; Compression
Compression=lzma2
SolidCompression=yes

; Interface
WizardStyle=modern
DisableWelcomePage=no

; Privilèges
PrivilegesRequired=lowest

; Langues
ShowLanguageDialog=auto

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
; Exécutable principal
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion

; Documentation
Source: "docs\README.md"; DestDir: "{app}\docs"; Flags: ignoreversion
Source: "docs\INSTALLATION.md"; DestDir: "{app}\docs"; Flags: ignoreversion
Source: "docs\QUICKSTART.md"; DestDir: "{app}\docs"; Flags: ignoreversion

; Icône
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.png"; DestDir: "{app}"; Flags: ignoreversion

; Fichier de version
Source: "VERSION.txt"; DestDir: "{app}"; Flags: ignoreversion

; NOTE: Ne pas utiliser "Flags: ignoreversion" sur des fichiers partagés système

[Icons]
; Raccourci dans le menu Démarrer
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\icon.ico"
Name: "{group}\Documentation"; Filename: "{app}\docs\README.md"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

; Raccourci sur le bureau (optionnel)
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\icon.ico"; Tasks: desktopicon

; Raccourci dans la barre de lancement rapide (optionnel)
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
; Proposer de lancer l'application à la fin de l'installation
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
// Script Pascal pour personnaliser l'installateur

function InitializeSetup(): Boolean;
begin
  Result := True;
  
  // Vérifier si une version est déjà installée
  if RegKeyExists(HKEY_CURRENT_USER, 'Software\{#MyAppName}') then
  begin
    if MsgBox('Une version de {#MyAppName} est déjà installée.' + #13#10 + 
              'Voulez-vous continuer l''installation ?', 
              mbConfirmation, MB_YESNO) = IDNO then
    begin
      Result := False;
    end;
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // Sauvegarder les informations d'installation dans le registre
    RegWriteStringValue(HKEY_CURRENT_USER, 'Software\{#MyAppName}', 
                        'InstallPath', ExpandConstant('{app}'));
    RegWriteStringValue(HKEY_CURRENT_USER, 'Software\{#MyAppName}', 
                        'Version', '{#MyAppVersion}');
  end;
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usPostUninstall then
  begin
    // Nettoyer le registre
    if RegKeyExists(HKEY_CURRENT_USER, 'Software\{#MyAppName}') then
    begin
      RegDeleteKeyIncludingSubkeys(HKEY_CURRENT_USER, 'Software\{#MyAppName}');
    end;
    
    // Demander si on supprime les sauvegardes
    if DirExists(ExpandConstant('{app}\data\backups')) then
    begin
      if MsgBox('Voulez-vous également supprimer les sauvegardes de la base de connaissances ?', 
                mbConfirmation, MB_YESNO) = IDYES then
      begin
        DelTree(ExpandConstant('{app}\data\backups'), True, True, True);
      end;
    end;
  end;
end;

[Registry]
; Enregistrer l'application pour la désinstallation
Root: HKCU; Subkey: "Software\{#MyAppName}"; Flags: uninsdeletekeyifempty
Root: HKCU; Subkey: "Software\{#MyAppName}"; ValueType: string; ValueName: "Version"; ValueData: "{#MyAppVersion}"
Root: HKCU; Subkey: "Software\{#MyAppName}"; ValueType: string; ValueName: "InstallPath"; ValueData: "{app}"

[UninstallDelete]
; Supprimer les fichiers temporaires créés par l'application
Type: filesandordirs; Name: "{app}\__pycache__"
Type: files; Name: "{app}\*.log"