import csv

def analyze_jobs(csv_file, target_skill):

    skill_count = 0
    jobs_with_skill = []
    
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                skills = [s.strip() for s in row['Skills'].split(',')]
                
                if target_skill.lower() in [s.lower() for s in skills]:
                    skill_count += 1
                    jobs_with_skill.append({
                        'Job': row['Job Title'],
                        'City': row['City']
                    })
                    
        # Display results
        print(f"\nAnalysis results for skill '{target_skill}':")
        print(f"Total matching jobs: {skill_count}")
        
        if skill_count > 0: # Found any
            print("\nMatching jobs:")
            for job in jobs_with_skill:
                print(f"- {job['Job']} in {job['City']}")
                
        # Saving results to text file
        with open('job_results.txt', 'w') as f:
            f.write(f"Analysis results for skill '{target_skill}':\n")
            f.write(f"Total matching jobs: {skill_count}\n\n")
            
            if skill_count > 0:
                f.write("Matching jobs:\n")
                for job in jobs_with_skill:
                    f.write(f"-{job['Job']} in {job['City']}\n")
                    
        print("\nResults saved to 'job_results.txt'.")
        
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    # input
    # target_skill = input("Enter skill to search for (ex : 'Python'): ").strip()
    target_skill = "Python"   #for using github actions
    
    if not target_skill:
        print("enter a skill to search for.")
    else:
        analyze_jobs("jobs.csv", target_skill)
