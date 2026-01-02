# check_rplidar.py
import sys

print("=" * 60)
print("RPLidar 0.9.2 패키지 분석")
print("=" * 60)

try:
    from rplidar import RPLidar
    
    print(f"\n✅ rplidar 패키지 임포트 성공")
    
    # RPLidar 클래스의 모든 메서드 출력
    print("\n📋 RPLidar 클래스의 모든 메서드:")
    all_methods = dir(RPLidar)
    
    public_methods = [m for m in all_methods if not m.startswith('_')]
    for method in sorted(public_methods):
        print(f"   - {method}")
    
    # 중요 메서드 확인
    print("\n🔍 필수 메서드 존재 여부:")
    required_methods = {
        'get_info': 'Device information',
        'get_health': 'Device health status',
        'clear_input': 'Clear serial buffer',
        'iter_scans': 'Iterate scans (recommended)',
        'iter_measurments': 'Iterate measurements (typo version)',
        'iter_measurements': 'Iterate measurements',
        'stop': 'Stop scanning',
        'stop_motor': 'Stop motor',
        'disconnect': 'Disconnect serial',
        'connect': 'Connect serial',
        'start_motor': 'Start motor'
    }
    
    for method, desc in required_methods.items():
        has_method = hasattr(RPLidar, method)
        status = "✅" if has_method else "❌"
        print(f"   {status} {method:<20} - {desc}")
    
    # 인스턴스 생성 테스트 (포트 없이)
    print("\n🔬 클래스 구조 확인:")
    print(f"   - __init__ 파라미터:")
    import inspect
    sig = inspect.signature(RPLidar.__init__)
    print(f"     {sig}")
    
except Exception as e:
    print(f"\n❌ 에러 발생: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)