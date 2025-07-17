import uuid
from datetime import datetime
from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, love_links

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_link():
    user_name = request.form.get('user_name', '').strip()
    crush_name = request.form.get('crush_name', '').strip()
    phone_number = request.form.get('phone_number', '').strip()
    
    if not user_name or not crush_name:
        flash('Please enter both names!', 'error')
        return redirect(url_for('index'))
    
    # Generate unique link ID
    link_id = str(uuid.uuid4())
    
    # Store the love link data
    love_links[link_id] = {
        'user_name': user_name,
        'crush_name': crush_name,
        'phone_number': phone_number,
        'created_at': datetime.now(),
        'response': None,
        'responded_at': None
    }
    
    # Generate the full URL
    love_url = request.host_url + 'love/' + link_id
    
    return render_template('response.html', 
                         love_url=love_url, 
                         user_name=user_name, 
                         crush_name=crush_name,
                         link_id=link_id)

@app.route('/love/<link_id>')
def love_message(link_id):
    if link_id not in love_links:
        flash('This love link doesn\'t exist or has expired!', 'error')
        return redirect(url_for('index'))
    
    link_data = love_links[link_id]
    
    # If already responded, show the response
    if link_data['response']:
        return render_template('love_message.html', 
                             link_data=link_data, 
                             link_id=link_id, 
                             already_responded=True)
    
    return render_template('love_message.html', 
                         link_data=link_data, 
                         link_id=link_id, 
                         already_responded=False)

@app.route('/respond/<link_id>', methods=['POST'])
def respond_to_love(link_id):
    if link_id not in love_links:
        flash('This love link doesn\'t exist or has expired!', 'error')
        return redirect(url_for('index'))
    
    response = request.form.get('response')
    if response not in ['yes', 'no', 'maybe']:
        flash('Invalid response!', 'error')
        return redirect(url_for('love_message', link_id=link_id))
    
    # Update the response
    love_links[link_id]['response'] = response
    love_links[link_id]['responded_at'] = datetime.now()
    
    return render_template('love_message.html', 
                         link_data=love_links[link_id], 
                         link_id=link_id, 
                         already_responded=True,
                         just_responded=True)

@app.route('/check/<link_id>')
def check_response(link_id):
    if link_id not in love_links:
        flash('This love link doesn\'t exist or has expired!', 'error')
        return redirect(url_for('index'))
    
    link_data = love_links[link_id]
    return render_template('response.html', 
                         link_data=link_data, 
                         link_id=link_id, 
                         checking=True)

@app.route('/api/check/<link_id>')
def api_check_response(link_id):
    if link_id not in love_links:
        return jsonify({'error': 'Link not found'}), 404
    
    link_data = love_links[link_id]
    return jsonify({
        'response': link_data['response'],
        'responded_at': link_data['responded_at'].isoformat() if link_data['responded_at'] else None
    })