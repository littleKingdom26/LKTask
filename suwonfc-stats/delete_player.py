#!/usr/bin/env python3
"""
선수 삭제 스크립트
사용법: python3 delete_player.py [선수 ID]
"""

import sys
import argparse
from player_model import get_all_players, delete_player, get_player_by_id

def list_players_for_selection():
    """선택을 위한 선수 목록"""
    players = get_all_players()
    
    print(f"\n{'='*70}")
    print("📋 선수 목록 (삭제 대상 선택)")
    print(f"{'='*70}\n")
    
    if not players:
        print("등록된 선수가 없습니다.")
        return []
    
    # 테이블 헤더
    header = f"{'ID':<5}{'번호':<6}{'이름':<15}{'포지션':<8}{'득점':<6}{'도움':<6}{'경기':<6}"
    print(header)
    print("-" * 70)
    
    # 선수 정보 출력
    player_list = []
    for player in players:
        row = f"{player.id:<5}{str(player.number):<6}{player.name:<15}{player.position:<8}{player.goals:<6}{player.assists:<6}{player.matches_played:<6}"
        print(row)
        player_list.append(player)
    
    print(f"\n{'='*70}")
    return player_list

def main():
    parser = argparse.ArgumentParser(description='선수 정보 삭제')
    parser.add_argument('--list', action='store_true', help='삭제 대상 선수 목록 보기')
    parser.add_argument('player_id', nargs='?', type=int, help='선수 ID')
    
    args = parser.parse_args()
    
    # 목록만 보기
    if args.list:
        list_players_for_selection()
        return
    
    # ID를 직접 지정
    if args.player_id:
        player_id = args.player_id
        
        # 삭제 전 선수 정보 확인
        player = get_player_by_id(player_id)
        if not player:
            print(f"⚠️ ID가 {player_id}인 선수를 찾을 수 없습니다.")
            return
        
        print(f"\n📋 삭제 대상: {player}")
        print(f"   ID: {player.id}")
        print(f"   이름: {player.name}")
        print(f"   득점: {player.goals}")
        print(f"   경기: {player.matches_played}")
        
        # 삭제 확인 (자동 진행)
        success = delete_player(player_id)
        
        if success:
            print(f"\n✅ 선수가 삭제되었습니다!")
            print(f"   ID: {player_id}")
            print(f"   이름: {player.name}")
        else:
            print(f"\n❌ 삭제에 실패했습니다.")
    else:
        # 아무것도 지정하지 않으면 목록 보기
        print("\n💡 삭제할 선수 ID를 지정해주세요.")
        print("   예: python3 delete_player.py 1")
        print("   또는: python3 delete_player.py --list")
        list_players_for_selection()

if __name__ == '__main__':
    main()
