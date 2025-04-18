#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v22
# autospec commit: 247c192
#
Name     : qt6serialbus
Version  : 6.9.0
Release  : 23
URL      : https://download.qt.io/official_releases/qt/6.9/6.9.0/submodules/qtserialbus-everywhere-src-6.9.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.9/6.9.0/submodules/qtserialbus-everywhere-src-6.9.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6serialbus-lib = %{version}-%{release}
Requires: qt6serialbus-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6serialbus package.
Group: Development
Requires: qt6serialbus-lib = %{version}-%{release}
Provides: qt6serialbus-devel = %{version}-%{release}
Requires: qt6serialbus = %{version}-%{release}

%description dev
dev components for the qt6serialbus package.


%package lib
Summary: lib components for the qt6serialbus package.
Group: Libraries
Requires: qt6serialbus-license = %{version}-%{release}

%description lib
lib components for the qt6serialbus package.


%package license
Summary: license components for the qt6serialbus package.
Group: Default

%description license
license components for the qt6serialbus package.


%prep
%setup -q -n qtserialbus-everywhere-src-6.9.0
cd %{_builddir}/qtserialbus-everywhere-src-6.9.0
pushd ..
cp -a qtserialbus-everywhere-src-6.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1743646532
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1743646532
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6serialbus
cp %{_builddir}/qtserialbus-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6serialbus/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtserialbus-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6serialbus/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtserialbus-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6serialbus/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtserialbus-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6serialbus/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtserialbus-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6serialbus/f45ee1c765646813b442ca58de72e20a64a7ddba || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qcanbusdevice_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qcanbusdeviceinfo_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qcandbcfileparser_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qcanframeprocessor_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qcanmessagedescription_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qcansignaldescription_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qcanuniqueiddescription_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qmodbus_symbols_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qmodbusadu_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qmodbusclient_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qmodbuscommevent_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qmodbusdevice_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qmodbusserver_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qmodbustcpclient_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qmodbustcpserver_p.h
/usr/include/QtSerialBus/6.9.0/QtSerialBus/private/qtserialbus-config_p.h
/usr/include/QtSerialBus/QCanBus
/usr/include/QtSerialBus/QCanBusDevice
/usr/include/QtSerialBus/QCanBusDeviceInfo
/usr/include/QtSerialBus/QCanBusFactory
/usr/include/QtSerialBus/QCanBusFrame
/usr/include/QtSerialBus/QCanDbcFileParser
/usr/include/QtSerialBus/QCanFrameProcessor
/usr/include/QtSerialBus/QCanMessageDescription
/usr/include/QtSerialBus/QCanSignalDescription
/usr/include/QtSerialBus/QCanUniqueIdDescription
/usr/include/QtSerialBus/QModbusClient
/usr/include/QtSerialBus/QModbusDataUnit
/usr/include/QtSerialBus/QModbusDataUnitMap
/usr/include/QtSerialBus/QModbusDevice
/usr/include/QtSerialBus/QModbusDeviceIdentification
/usr/include/QtSerialBus/QModbusExceptionResponse
/usr/include/QtSerialBus/QModbusPdu
/usr/include/QtSerialBus/QModbusReply
/usr/include/QtSerialBus/QModbusRequest
/usr/include/QtSerialBus/QModbusResponse
/usr/include/QtSerialBus/QModbusServer
/usr/include/QtSerialBus/QModbusTcpClient
/usr/include/QtSerialBus/QModbusTcpConnectionObserver
/usr/include/QtSerialBus/QModbusTcpServer
/usr/include/QtSerialBus/QtSerialBus
/usr/include/QtSerialBus/QtSerialBusDepends
/usr/include/QtSerialBus/QtSerialBusVersion
/usr/include/QtSerialBus/qcanbus.h
/usr/include/QtSerialBus/qcanbusdevice.h
/usr/include/QtSerialBus/qcanbusdeviceinfo.h
/usr/include/QtSerialBus/qcanbusfactory.h
/usr/include/QtSerialBus/qcanbusframe.h
/usr/include/QtSerialBus/qcancommondefinitions.h
/usr/include/QtSerialBus/qcandbcfileparser.h
/usr/include/QtSerialBus/qcanframeprocessor.h
/usr/include/QtSerialBus/qcanmessagedescription.h
/usr/include/QtSerialBus/qcansignaldescription.h
/usr/include/QtSerialBus/qcanuniqueiddescription.h
/usr/include/QtSerialBus/qmodbusclient.h
/usr/include/QtSerialBus/qmodbusdataunit.h
/usr/include/QtSerialBus/qmodbusdevice.h
/usr/include/QtSerialBus/qmodbusdeviceidentification.h
/usr/include/QtSerialBus/qmodbuspdu.h
/usr/include/QtSerialBus/qmodbusreply.h
/usr/include/QtSerialBus/qmodbusserver.h
/usr/include/QtSerialBus/qmodbustcpclient.h
/usr/include/QtSerialBus/qmodbustcpserver.h
/usr/include/QtSerialBus/qtserialbus-config.h
/usr/include/QtSerialBus/qtserialbusexports.h
/usr/include/QtSerialBus/qtserialbusglobal.h
/usr/include/QtSerialBus/qtserialbusversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtSerialBusTestsConfig.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PassThruCanBusPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PassThruCanBusPluginConfig.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PassThruCanBusPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PassThruCanBusPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PassThruCanBusPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PassThruCanBusPluginTargets.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PeakCanBusPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PeakCanBusPluginConfig.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PeakCanBusPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PeakCanBusPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PeakCanBusPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6PeakCanBusPluginTargets.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SerialBusAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SerialBusConfig.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SerialBusConfigVersion.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SerialBusConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SerialBusDependencies.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SerialBusPlugins.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SerialBusTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SerialBusTargets.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SerialBusVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SerialBusVersionlessTargets.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SocketCanBusPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SocketCanBusPluginConfig.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SocketCanBusPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SocketCanBusPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SocketCanBusPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6SocketCanBusPluginTargets.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6TinyCanBusPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6TinyCanBusPluginConfig.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6TinyCanBusPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6TinyCanBusPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6TinyCanBusPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6TinyCanBusPluginTargets.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6VirtualCanBusPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6VirtualCanBusPluginConfig.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6VirtualCanBusPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6VirtualCanBusPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6VirtualCanBusPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6SerialBus/Qt6VirtualCanBusPluginTargets.cmake
/usr/lib64/cmake/Qt6SerialBusPrivate/Qt6SerialBusPrivateAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6SerialBusPrivate/Qt6SerialBusPrivateConfig.cmake
/usr/lib64/cmake/Qt6SerialBusPrivate/Qt6SerialBusPrivateConfigVersion.cmake
/usr/lib64/cmake/Qt6SerialBusPrivate/Qt6SerialBusPrivateConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6SerialBusPrivate/Qt6SerialBusPrivateDependencies.cmake
/usr/lib64/cmake/Qt6SerialBusPrivate/Qt6SerialBusPrivateTargets.cmake
/usr/lib64/cmake/Qt6SerialBusPrivate/Qt6SerialBusPrivateVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6SerialBusPrivate/Qt6SerialBusPrivateVersionlessTargets.cmake
/usr/lib64/libQt6SerialBus.prl
/usr/lib64/libQt6SerialBus.so
/usr/lib64/pkgconfig/Qt6SerialBus.pc
/usr/lib64/qt6/mkspecs/modules/qt_lib_serialbus.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_serialbus_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6SerialBus.so.6.9.0
/V3/usr/lib64/qt6/bin/canbusutil
/V3/usr/lib64/qt6/plugins/canbus/libqtpassthrucanbus.so
/V3/usr/lib64/qt6/plugins/canbus/libqtpeakcanbus.so
/V3/usr/lib64/qt6/plugins/canbus/libqtsocketcanbus.so
/V3/usr/lib64/qt6/plugins/canbus/libqttinycanbus.so
/V3/usr/lib64/qt6/plugins/canbus/libqtvirtualcanbus.so
/usr/lib64/libQt6SerialBus.so.6
/usr/lib64/libQt6SerialBus.so.6.9.0
/usr/lib64/qt6/bin/canbusutil
/usr/lib64/qt6/metatypes/qt6serialbus_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/SerialBus.json
/usr/lib64/qt6/plugins/canbus/libqtpassthrucanbus.so
/usr/lib64/qt6/plugins/canbus/libqtpeakcanbus.so
/usr/lib64/qt6/plugins/canbus/libqtsocketcanbus.so
/usr/lib64/qt6/plugins/canbus/libqttinycanbus.so
/usr/lib64/qt6/plugins/canbus/libqtvirtualcanbus.so
/usr/lib64/qt6/sbom/qtserialbus-6.9.0.spdx

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6serialbus/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6serialbus/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6serialbus/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6serialbus/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6serialbus/f45ee1c765646813b442ca58de72e20a64a7ddba
