; Script Inno Setup pour Système Expert - Droit du Numérique
; Nécessite Inno Setup 6.0 ou supérieur
; Télécharger : https://jrsoftware.org/isdl.php

#define MyAppName "Système Expert - Droit du Numérique"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Système Expert Académique"
#define MyAppURL "https://github.com/Brice97426/systeme-expert-droit-numerique"
#define MyAppExeName "SystemeExpertDroitNumerique.exe"

[Setup]
; Informations de l'application
AppId={{A5B8C3D4-E6F7-4A1B-9C2D-3E4F5A6B7C8D}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}/issues
AppUpdatesURL={#MyAppURL}/releases
AppCopyright=Copyright © 2024 {#MyAppPublisher}

; Répertoire d'installation par défaut
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes

; Fichier de sortie
OutputDir=installer_output
OutputBaseFilename=SystemeExpertDroitNumerique_Setup_v{#MyAppVersion}

; Icône de l'installateur
SetupIconFile=icon.ico

; Compression
Compression=lzma2/ultra64
SolidCompression=yes

; Interface
WizardStyle=modern
DisableWelcomePage=no
WizardImageFile=compiler:WizModernImage-IS.bmp
WizardSmallImageFile=compiler:WizModernSmallImage-IS.bmp

; Privilèges
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog

; Langues
ShowLanguageDialog=auto

; Informations de version
VersionInfoVersion={#MyAppVersion}
VersionInfoCompany={#MyAppPublisher}
VersionInfoDescription=Système expert d'aide à la décision en droit du numérique
VersionInfoCopyright=Copyright © 2024 {#MyAppPublisher}
VersionInfoProductName={#MyAppName}
VersionInfoProductVersion={#MyAppVersion}

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
; Exécutable principal (depuis le dossier dist/ créé par PyInstaller)
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion

; Documentation principale
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion isreadme
Source: "LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "CHANGELOG.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "CONTRIBUTING.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "SECURITY.md"; DestDir: "{app}"; Flags: ignoreversion

; Documentation du dossier docs/
Source: "docs\INSTALLATION.md"; DestDir: "{app}\docs"; Flags: ignoreversion
Source: "docs\*.md"; DestDir: "{app}\docs"; Flags: ignoreversion

; Icônes
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.png"; DestDir: "{app}"; Flags: ignoreversion

; Fichier de version
Source: "Version.txt"; DestDir: "{app}"; Flags: ignoreversion

; NOTE: La base de connaissances est déjà incluse dans l'exécutable PyInstaller
; Si vous voulez la distribuer séparément :
; Source: "data\legal_expert_system_kb.json"; DestDir: "{app}\data"; Flags: ignoreversion

[Icons]
; Raccourci dans le menu Démarrer
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\icon.ico"; Comment: "Lancer le système expert"
Name: "{group}\Documentation"; Filename: "{app}\README.md"; Comment: "Consulter la documentation"
Name: "{group}\Guide d'installation"; Filename: "{app}\docs\INSTALLATION.md"; Comment: "Guide d'installation détaillé"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"; Comment: "Désinstaller l'application"

; Raccourci sur le bureau (optionnel)
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\icon.ico"; Tasks: desktopicon; Comment: "Lancer le système expert"

; Raccourci dans la barre de lancement rapide (optionnel, anciennes versions Windows)
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
; Proposer de lancer l'application à la fin de l'installation
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

; Proposer d'ouvrir le README
Filename: "{app}\README.md"; Description: "Lire la documentation"; Flags: postinstall shellexec skipifsilent unchecked

[Code]
// Variables globales
var
  DataDirPage: TInputDirWizardPage;

// Fonction d'initialisation de l'installation
function InitializeSetup(): Boolean;
begin
  Result := True;
  
  // Vérifier si une version est déjà installée
  if RegKeyExists(HKEY_CURRENT_USER, 'Software\{#MyAppName}') then
  begin
    if MsgBox('Une version de {#MyAppName} est déjà installée.' + #13#10 + 
              'Voulez-vous continuer l''installation ?' + #13#10 + #13#10 +
              'Note : L''ancienne version sera désinstallée automatiquement.', 
              mbConfirmation, MB_YESNO or MB_DEFBUTTON2) = IDNO then
    begin
      Result := False;
      Exit;
    end;
  end;
  
  // Vérification de l'espace disque (100 MB minimum)
  if GetSpaceOnDisk(ExpandConstant('{app}'), False, nil, nil, nil) < 104857600 then
  begin
    MsgBox('Espace disque insuffisant.' + #13#10 +
           'Au moins 100 MB d''espace libre sont nécessaires.', 
           mbError, MB_OK);
    Result := False;
  end;
end;

// Actions après l'installation
procedure CurStepChanged(CurStep: TSetupStep);
var
  Version: String;
begin
  if CurStep = ssPostInstall then
  begin
    // Sauvegarder les informations d'installation dans le registre
    RegWriteStringValue(HKEY_CURRENT_USER, 'Software\{#MyAppName}', 
                        'InstallPath', ExpandConstant('{app}'));
    RegWriteStringValue(HKEY_CURRENT_USER, 'Software\{#MyAppName}', 
                        'Version', '{#MyAppVersion}');
    RegWriteStringValue(HKEY_CURRENT_USER, 'Software\{#MyAppName}', 
                        'InstallDate', GetDateTimeString('yyyy-mm-dd hh:nn:ss', '-', ':'));
                        
    // Log de l'installation
    Log('Installation terminée avec succès');
    Log('Version installée : {#MyAppVersion}');
    Log('Chemin d''installation : ' + ExpandConstant('{app}'));
  end;
end;

// Actions avant la désinstallation
function InitializeUninstall(): Boolean;
var
  Response: Integer;
begin
  Result := True;
  
  Response := MsgBox('Êtes-vous sûr de vouloir désinstaller {#MyAppName} ?' + #13#10 + #13#10 +
                     'Cette action supprimera l''application mais conservera vos données si vous en avez.',
                     mbConfirmation, MB_YESNO or MB_DEFBUTTON2);
  
  if Response = IDNO then
    Result := False;
end;

// Actions après la désinstallation
procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usPostUninstall then
  begin
    // Nettoyer le registre
    if RegKeyExists(HKEY_CURRENT_USER, 'Software\{#MyAppName}') then
    begin
      Log('Suppression des clés de registre');
      RegDeleteKeyIncludingSubkeys(HKEY_CURRENT_USER, 'Software\{#MyAppName}');
    end;
    
    // Demander si l'utilisateur veut supprimer les données/backups
    if DirExists(ExpandConstant('{app}\data\backups')) then
    begin
      if MsgBox('Voulez-vous également supprimer les sauvegardes de la base de connaissances ?' + #13#10 +
                'Chemin : ' + ExpandConstant('{app}\data\backups'), 
                mbConfirmation, MB_YESNO) = IDYES then
      begin
        Log('Suppression des sauvegardes');
        DelTree(ExpandConstant('{app}\data\backups'), True, True, True);
      end
      else
      begin
        Log('Sauvegardes conservées par l''utilisateur');
      end;
    end;
    
    // Message de confirmation
    MsgBox('Désinstallation terminée.' + #13#10 + #13#10 +
           'Merci d''avoir utilisé {#MyAppName} !', 
           mbInformation, MB_OK);
  end;
end;

[Registry]
; Enregistrer l'application dans le registre Windows
Root: HKCU; Subkey: "Software\{#MyAppName}"; Flags: uninsdeletekeyifempty
Root: HKCU; Subkey: "Software\{#MyAppName}"; ValueType: string; ValueName: "Version"; ValueData: "{#MyAppVersion}"
Root: HKCU; Subkey: "Software\{#MyAppName}"; ValueType: string; ValueName: "InstallPath"; ValueData: "{app}"
Root: HKCU; Subkey: "Software\{#MyAppName}"; ValueType: string; ValueName: "Executable"; ValueData: "{app}\{#MyAppExeName}"

[UninstallDelete]
; Supprimer les fichiers temporaires créés par l'application
Type: filesandordirs; Name: "{app}\__pycache__"
Type: files; Name: "{app}\*.log"
Type: files; Name: "{app}\*.tmp"
Type: filesandordirs; Name: "{localappdata}\{#MyAppName}\Cache"

[Messages]
; Messages personnalisés en français
french.WelcomeLabel2=Ceci installera [name/ver] sur votre ordinateur.%n%nCe système expert est un outil pédagogique destiné à l'apprentissage du droit du numérique. Il ne remplace pas un avocat spécialisé.%n%nIl est recommandé de fermer toutes les autres applications avant de continuer.
french.FinishedLabel=L'installation de [name] est terminée. L'application peut être lancée en sélectionnant les raccourcis installés.

[CustomMessages]
; Messages personnalisés
french.AppDescription=Système expert d'aide à la décision en droit du numérique
french.LegalWarning=⚠️ Cet outil est à but pédagogique uniquement
french.RequirementsNotMet=Configuration système insuffisante
french.CloseApplications=Veuillez fermer toutes les instances de l'application