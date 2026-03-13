#!/usr/bin/env python3
"""
선수 통계 분석 스크립트
사용법: python3 stats.py
"""

from player_model import get_all_players

def calculate_stats():
    """통계 계산"""
    players = get_all_players()
    
    if not players:
        print("⚠️ 등록된 선수가 없습니다.")
        return
    
    print(f"\n{'='*70}")
    print("📊 선수 통계")
    print(f"{'='*70}\n")
    
    # 1. 득점 순위
    print("⚽ 득점 순위")
    print("-" * 70)
    goals_ranking = sorted(players, key=lambda x: x.goals, reverse=True)
    for idx, player in enumerate(goals_ranking, 1):
        if player.goals > 0:
            goal_rate = player.goals / player.matches_played if player.matches_played > 0 else 0
            print(f"{idx:2}. {player.name:15} ({player.position:3}) - {player.goals:2}골 ({goal_rate:.2f} 골/경기)")
    
    # 2. 도움 순위
    print("\n🎯 도움 순위")
    print("-" * 70)
    assists_ranking = sorted(players, key=lambda x: x.assists, reverse=True)
    for idx, player in enumerate(assists_ranking, 1):
        if player.assists > 0:
            assist_rate = player.assists / player.matches_played if player.matches_played > 0 else 0
            print(f"{idx:2}. {player.name:15} ({player.position:3}) - {player.assists:2}도움 ({assist_rate:.2f} 도움/경기)")
    
    # 3. 출전 시간 순위
    print("\n⏱️ 출전 시간 순위")
    print("-" * 70)
    time_ranking = sorted(players, key=lambda x: x.minutes_played, reverse=True)
    for idx, player in enumerate(time_ranking, 1):
        if player.minutes_played > 0:
            avg_minutes = player.minutes_played / player.matches_played if player.matches_played > 0 else 0
            print(f"{idx:2}. {player.name:15} ({player.position:3}) - {player.minutes_played:5}분 (평균 {avg_minutes:.1f}분/경기)")
    
    # 4. 포지션별 분석
    print("\n🔍 포지션별 분석")
    print("-" * 70)
    positions = ['FW', 'MF', 'DF', 'GK']
    for pos in positions:
        pos_players = [p for p in players if p.position == pos]
        if pos_players:
            total_goals = sum(p.goals for p in pos_players)
            total_assists = sum(p.assists for p in pos_players)
            avg_goals = total_goals / len(pos_players)
            print(f"{pos:3} - {len(pos_players):2}명 | 총 득점: {total_goals:2} | 평균: {avg_goals:.2f} | 총 도움: {total_assists:2}")
    
    # 5. 종합 통계
    print("\n📈 종합 통계")
    print("-" * 70)
    total_goals = sum(p.goals for p in players)
    total_assists = sum(p.assists for p in players)
    total_matches = sum(p.matches_played for p in players)
    total_yellow = sum(p.yellow_cards for p in players)
    total_red = sum(p.red_cards for p in players)
    
    print(f"총 선수: {len(players)}명")
    print(f"총 득점: {total_goals}골")
    print(f"총 도움: {total_assists}도움")
    print(f"총 경기: {total_matches}경기")
    print(f"총 노란 카드: {total_yellow}장")
    print(f"총 빨간 카드: {total_red}장")
    print(f"평균 득점: {total_goals / len(players) if len(players) > 0 else 0:.2f}골/선수")
    print(f"평균 도움: {total_assists / len(players) if len(players) > 0 else 0:.2f}도움/선수")
    
    print(f"\n{'='*70}\n")

if __name__ == '__main__':
    calculate_stats()
